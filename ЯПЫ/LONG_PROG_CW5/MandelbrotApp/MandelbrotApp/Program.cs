using System;
using System.Runtime.InteropServices;
using Raylib_cs;
using Python.Runtime;

namespace MandelbrotApp
{
    class Program
    {
        const int ScreenWidth = 800;
        const int ScreenHeight = 600;

        static void Main(string[] args)
        {
            // === Настройка Python для macOS + pyenv ===
            const string pythonHome = "/Users/maria/.pyenv/versions/3.11.9";
            const string libpythonPath = pythonHome + "/lib/libpython3.11.dylib";

            // Обязательно для pythonnet >= 3.0
            Python.Runtime.Runtime.PythonDLL = libpythonPath;

            Environment.SetEnvironmentVariable("PYTHONHOME", pythonHome);
            Environment.SetEnvironmentVariable("DYLD_LIBRARY_PATH", pythonHome + "/lib");

            // Инициализация Python
            PythonEngine.Initialize();

            // Загружаем модуль fractal.py внутри GIL
            dynamic fractalModule;
            using (Py.GIL())
            {
                dynamic sys = Py.Import("sys");
                sys.path.append(AppDomain.CurrentDomain.BaseDirectory);
                fractalModule = Py.Import("fractal");
            }

            // === Инициализация Raylib ===
            Raylib.InitWindow(ScreenWidth, ScreenHeight, "Mandelbrot via Python.NET");
            Raylib.SetTargetFPS(60);

            var image = Raylib.GenImageColor(ScreenWidth, ScreenHeight, Color.Black);
            var texture = Raylib.LoadTextureFromImage(image);
            Raylib.UnloadImage(image);

            double zoom = 1.0;
            const double centerX = -0.74920463346;
            const double centerY = 0.00000000123;

            var pixelData = new uint[ScreenWidth * ScreenHeight];
            var handle = GCHandle.Alloc(pixelData, GCHandleType.Pinned);

            try
            {
                while (!Raylib.WindowShouldClose())
                {
                    zoom *= 1.02;

                    // === Вызов Python-функции ===
                    byte[] pixelBytes;
                    using (Py.GIL())
                    {
                        pixelBytes = fractalModule.render_mandelbrot(
                            ScreenWidth, ScreenHeight, zoom, centerX, centerY
                        );
                    }

                    // Копируем байты в uint[]
                    Buffer.BlockCopy(pixelBytes, 0, pixelData, 0, pixelBytes.Length);

                    // Обновляем текстуру (требует unsafe)
                    unsafe
                    {
                        Raylib.UpdateTexture(texture, (void*)handle.AddrOfPinnedObject());
                    }

                    // === Рендеринг ===
                    Raylib.BeginDrawing();
                    Raylib.ClearBackground(Color.Black);
                    Raylib.DrawTexture(texture, 0, 0, Color.White);
                    Raylib.DrawFPS(10, 10);
                    Raylib.DrawText($"Zoom: {zoom:E2}", 10, 30, 20, Color.White);
                    Raylib.EndDrawing();
                }
            }
            finally
            {
                handle.Free();
                Raylib.UnloadTexture(texture);
                Raylib.CloseWindow();
                PythonEngine.Shutdown();
            }
        }
    }
}