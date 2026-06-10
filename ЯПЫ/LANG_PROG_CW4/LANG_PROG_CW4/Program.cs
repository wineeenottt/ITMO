using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        if (args.Length != 2)
        {
            Console.WriteLine("Используются: <port> <document_root>");
            return;
        }

        if (!int.TryParse(args[0], out int port) || port <= 0 || port > 65535)
        {
            Console.WriteLine("Ошибка порта");
            return;
        }

        string documentRoot = Path.GetFullPath(args[1]);
        if (!Directory.Exists(documentRoot))
        {
            Console.WriteLine($"Директория не найдена: {documentRoot}");
            return;
        }

        Console.WriteLine($"Директория: {documentRoot}, порт: {port}");

        TcpListener listener = new TcpListener(System.Net.IPAddress.Any, port);
        listener.Start();

        try
        {
            while (true)
            {
                TcpClient client = await listener.AcceptTcpClientAsync();
                _ = Task.Run(() => HandleClientAsync(client, documentRoot));
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Server error: {ex.Message}");
        }
        finally
        {
            listener.Stop();
        }
    }

    static async Task HandleClientAsync(TcpClient client, string documentRoot)
    {
        using (client)
        using (var stream = client.GetStream())
        {
            try
            {
                byte[] buffer = new byte[4096];
                int bytesRead = await stream.ReadAsync(buffer, 0, buffer.Length);
                if (bytesRead == 0) return;

                string request = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                Console.WriteLine("Request:\n" + request);
                
                var match = Regex.Match(request, @"^GET\s+([^\s]+)");
                if (!match.Success)
                {
                    await SendErrorResponse(stream, 400, "Bad Request");
                    return;
                }

                string rawPath = match.Groups[1].Value;
                
                string decodedPath = Uri.UnescapeDataString(rawPath).TrimStart('/');
                string fullPath = Path.GetFullPath(Path.Combine(documentRoot, decodedPath));

                if (!fullPath.StartsWith(documentRoot, StringComparison.OrdinalIgnoreCase))
                {
                    await SendErrorResponse(stream, 403, "Forbidden");
                    return;
                }
                
                if (Directory.Exists(fullPath))
                {
                    fullPath = Path.Combine(fullPath, "index.html");
                }

                if (!File.Exists(fullPath))
                {
                    await SendErrorResponse(stream, 404, "Not Found");
                    return;
                }
                
                string mimeType = GetMimeType(Path.GetExtension(fullPath));
                
                var fileInfo = new FileInfo(fullPath);
                string headers = $"HTTP/1.1 200 OK\r\n" +
                                 $"Content-Type: {mimeType}\r\n" +
                                 $"Content-Length: {fileInfo.Length}\r\n" +
                                 "Connection: close\r\n" +
                                 "\r\n";

                await stream.WriteAsync(Encoding.UTF8.GetBytes(headers));
                
                using var fileStream = new FileStream(
                    fullPath,
                    FileMode.Open,
                    FileAccess.Read,
                    FileShare.Read,
                    bufferSize: 65536 
                );

                await fileStream.CopyToAsync(stream);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка клиента: {ex}");
            }
        }
    }

    static async Task SendErrorResponse(NetworkStream stream, int statusCode, string statusText)
    {
        string body = $"{statusCode} {statusText}";
        byte[] bodyBytes = Encoding.UTF8.GetBytes(body);
        string response = $"HTTP/1.1 {statusCode} {statusText}\r\n" +
                          "Content-Type: text/plain; charset=utf-8\r\n" +
                          $"Content-Length: {bodyBytes.Length}\r\n" +
                          "Connection: close\r\n" +
                          "\r\n";

        byte[] responseBytes = Encoding.UTF8.GetBytes(response);
        await stream.WriteAsync(responseBytes, 0, responseBytes.Length);
        await stream.WriteAsync(bodyBytes, 0, bodyBytes.Length);
    }

    static string GetMimeType(string extension)
    {
        return extension.ToLowerInvariant() switch
        {
            ".html" or ".htm" => "text/html",
            ".css" => "text/css",
            ".js" => "application/javascript",
            ".json" => "application/json",
            ".png" => "image/png",
            ".jpg" or ".jpeg" => "image/jpeg",
            ".gif" => "image/gif",
            ".svg" => "image/svg+xml",
            ".txt" => "text/plain",
            ".pdf" => "application/pdf",
            ".zip" => "application/zip",
            _ => "application/octet-stream"
        };
    }
}