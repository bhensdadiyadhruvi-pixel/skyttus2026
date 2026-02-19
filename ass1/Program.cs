
using System;
using System.Collections.Generic;
using System.Linq;

class Student
{
    // Encapsulation (Properties)
    public int StudentId { get; set; }
    public string Name { get; set; }
    public string Department { get; set; }
    public int Year { get; set; }
    public int Marks { get; set; }

    // Constructor
    public Student(int id, string name, string dept, int year, int marks)
    {
        StudentId = id;
        Name = name;
        Department = dept;
        Year = year;
        Marks = marks;
    }

    // Method to display student info
    public void Display()
    {
        Console.WriteLine($"{StudentId} | {Name} | {Department} | Year {Year} | Marks: {Marks}");
    }
}

class Program
{
    static void Main(string[] args)
    {
        List<Student> students = new List<Student>();

        Console.Write("Enter number of students: ");
        int n = int.Parse(Console.ReadLine() ?? "0");

        // Create multiple student objects
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine($"\nEnter details for Student {i + 1}");

            Console.Write("Student ID: ");
            int id = int.Parse(Console.ReadLine() ?? "0");

            Console.Write("Name: ");
            string name = Console.ReadLine() ?? "";

            Console.Write("Department: ");
            string dept = Console.ReadLine() ?? "";

            Console.Write("Year: ");
            int year = int.Parse(Console.ReadLine() ?? "0");

            Console.Write("Marks: ");
            int marks = int.Parse(Console.ReadLine() ?? "0");

            students.Add(new Student(id, name, dept, year, marks));
        }

        // 5️⃣ Display all records
        Console.WriteLine("\n--- All Student Records ---");
        foreach (var s in students)
        {
            s.Display();
        }

        // 6️⃣ Students with marks > 75
        Console.WriteLine("\n--- Students with Marks > 75 ---");
        var highScorers = students.Where(s => s.Marks > 75);
        foreach (var s in highScorers)
        {
            s.Display();
        }

        // 7️⃣ Sort students by marks (Descending)
        var sortedStudents = students.OrderByDescending(s => s.Marks).ToList();

        Console.WriteLine("\n--- Students Sorted by Marks (Descending) ---");
        foreach (var s in sortedStudents)
        {
            s.Display();
        }

        // 8️⃣ Top 3 Scorers
        Console.WriteLine("\n--- Top 3 Scorers ---");
        foreach (var s in sortedStudents.Take(3))
        {
            s.Display();
        }

        Console.ReadLine();
    }
}

