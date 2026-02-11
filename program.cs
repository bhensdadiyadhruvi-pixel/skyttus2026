using System;

class StudentDetails
{
    public int student_id;
    public string name = "";
    public string department = "";
    public int marks;
}

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Enter number of students: ");
        int n = int.Parse(Console.ReadLine() ?? "0");

        StudentDetails[] students = new StudentDetails[n];

        // 1️⃣ Accept student details
        for (int i = 0; i < n; i++)
        {
            students[i] = new StudentDetails();

            Console.WriteLine("\nEnter details for Student " + (i + 1));

            Console.Write("Student ID: ");
            students[i].student_id = int.Parse(Console.ReadLine() ?? "0");

            Console.Write("Name: ");
            students[i].name = Console.ReadLine() ?? "";

            Console.Write("Department: ");
            students[i].department = Console.ReadLine() ?? "";

            Console.Write("Marks: ");
            students[i].marks = int.Parse(Console.ReadLine() ?? "0");
        }

        // 2️⃣ Display all student records
        Console.WriteLine("\n--- All Student Records ---");
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine(students[i].student_id + " | " +
                              students[i].name + " | " +
                              students[i].department + " | " +
                              students[i].marks);
        }

        // 3️⃣ Display only name and department
        Console.WriteLine("\n--- Name and Department ---");
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine(students[i].name + " - " + students[i].department);
        }

        // 4️⃣ Students with marks > 75
        Console.WriteLine("\n--- Students with Marks > 75 ---");
        for (int i = 0; i < n; i++)
        {
            if (students[i].marks > 75)
            {
                Console.WriteLine(students[i].name + " - " + students[i].marks);
            }
        }

        // 5️⃣ Students from specific department
        Console.Write("\nEnter department to search: ");
        string deptSearch = Console.ReadLine() ?? "";

        Console.WriteLine("--- Students from " + deptSearch + " Department ---");
        for (int i = 0; i < n; i++)
        {
            if (students[i].department.ToLower() == deptSearch.ToLower())
            {
                Console.WriteLine(students[i].name + " - " + students[i].marks);
            }
        }

        // 6️⃣ Sort students by marks (Descending)
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (students[i].marks < students[j].marks)
                {
                    StudentDetails temp = students[i];
                    students[i] = students[j];
                    students[j] = temp;
                }
            }
        }

        Console.WriteLine("\n--- Students Sorted by Marks (Descending) ---");
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine(students[i].name + " - " + students[i].marks);
        }

        // 7️⃣ Top Scorer
        if (n > 0)
        {
            Console.WriteLine("\n--- Top Scorer ---");
            Console.WriteLine(students[0].name + " with " + students[0].marks + " marks");
        }

        Console.ReadLine();
    }
}