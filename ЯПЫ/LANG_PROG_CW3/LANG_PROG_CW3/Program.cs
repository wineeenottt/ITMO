using Microsoft.EntityFrameworkCore;

namespace LANG_PROG_CW3
{
    public class GradeRecord
    {
        public int Id { get; set; }
        public string StudentName { get; set; } = null!;
        public string Subject { get; set; } = null!;
        public int Mark { get; set; }
    }

    public class GradebookContext : DbContext
    {
        public DbSet<GradeRecord> GradeRecords { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseNpgsql("Host=localhost;Port=5432;Database=studs;Username=s466310;Password=****");
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<GradeRecord>(entity =>
            {
                entity.ToTable("grade_records");
            });
        }
    }

    class Program
    {
        static void Main()
        {
            using (var initDb = new GradebookContext())
            {
                initDb.Database.EnsureCreated(); 
            }

            bool exit = false;
            while (!exit)
            {
                Console.WriteLine("\n Меню журнала оценок: ");
                Console.WriteLine("1. Добавить запись");
                Console.WriteLine("2. Удалить запись по студенту и предмету");
                Console.WriteLine("3. Поиск по предмету");
                Console.WriteLine("4. Выход");
                Console.Write("Выберете: ");
                string? choice = Console.ReadLine();

                switch (choice)
                {
                    case "1": AddRecord(); break;
                    case "2": DeleteRecord(); break;
                    case "3": SearchBySubject(); break;
                    case "4": exit = true; break;
                    default: Console.WriteLine("Неверный выбор"); break;
                }
            }
        }

        static void AddRecord()
        {
            Console.Write("Введите имя студента: ");
            string student = Console.ReadLine() ?? "";
            Console.Write("Введите название предмета: ");
            string subject = Console.ReadLine() ?? "";
            Console.Write("Введите оценку: ");
            if (!int.TryParse(Console.ReadLine(), out int mark))
            {
                Console.WriteLine("Некорректная оценка");
                return;
            }
            
            if (string.IsNullOrWhiteSpace(student))
            {
                Console.WriteLine("Имя студента пустое");
                return;
            }
            if (string.IsNullOrWhiteSpace(subject))
            {
                Console.WriteLine("Название предмета пустое");
                return;
            }
            if (mark < 1 || mark > 5)
            {
                Console.WriteLine("Оценка должна быть от 1 до 5");
                return;
            }

            using (var db = new GradebookContext())
            {
                var record = new GradeRecord { StudentName = student, Subject = subject, Mark = mark };
                db.GradeRecords.Add(record);
                db.SaveChanges();
            }

            Console.WriteLine("Запись успешно добавлена");
        }

        static void DeleteRecord()
        {
            Console.Write("Введите имя студента: ");
            string student = Console.ReadLine() ?? "";
            Console.Write("Введите название предмета: ");
            string subject = Console.ReadLine() ?? "";
            
            if (string.IsNullOrWhiteSpace(student) || string.IsNullOrWhiteSpace(subject))
            {
                Console.WriteLine("Имя студента и названия предмета пустые");
                return;
            }

            using (var db = new GradebookContext())
            {
                var record = db.GradeRecords
                    .FirstOrDefault(r =>
                        EF.Functions.ILike(r.StudentName, student) &&
                        EF.Functions.ILike(r.Subject, subject));

                if (record != null)
                {
                    db.GradeRecords.Remove(record);
                    db.SaveChanges();
                    Console.WriteLine("Запись удалена");
                }
                else
                {
                    Console.WriteLine("Запись не найдена");
                }
            }
        }

        static void SearchBySubject()
        {
            Console.Write("Введите название предмета: ");
            string subject = Console.ReadLine() ?? "";
            
            if (string.IsNullOrWhiteSpace(subject))
            {
                Console.WriteLine("Название предмета пустое");
                return;
            }

            using (var db = new GradebookContext())
            {
                var results = db.GradeRecords
                    .Where(r => EF.Functions.ILike(r.Subject, subject))
                    .OrderBy(r => r.StudentName)
                    .ToList();

                if (results.Count == 0)
                {
                    Console.WriteLine("Записи по данному предменту не найдены");
                    return;
                }

                Console.WriteLine($"\nОценки по предмету '{subject}':");
                foreach (var r in results)
                {
                    Console.WriteLine($"{r.StudentName} — {r.Mark}");
                }
            }
        }
    }
}