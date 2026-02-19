using Microsoft.AspNetCore.Mvc;
using MvcStudentApp.Models;
using System.Collections.Generic;

namespace MvcStudentApp.Controllers
{
    public class StudentController : Controller
    {
        public IActionResult Index()
        {
            var students = new List<Student>
            {
                new Student { Id = 1, Name = "Dhruvi", Age = 20, Course = "BCA" },
                new Student { Id = 2, Name = "Kittu", Age = 21, Course = "BBA" },
                new Student { Id = 3, Name = "Yug", Age = 22, Course = "B.Tech" }
            };

            return View(students);
        }
    }
}