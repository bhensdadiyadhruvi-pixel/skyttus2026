using Microsoft.AspNetCore.Mvc;
using MvcCrudApp.Models;
using System.Collections.Generic;
using System.Linq;

namespace MvcCrudApp.Controllers
{
    public class StudentController : Controller
    {
        // Temporary in-memory list (instead of database)
        private static List<Student> students = new List<Student>();
        private static int nextId = 1;

        // READ (List)
        public IActionResult Index()
        {
            return View(students);
        }

        // CREATE - GET
        public IActionResult Create()
        {
            return View();
        }

        // CREATE - POST
        [HttpPost]
        public IActionResult Create(Student student)
        {
            if (ModelState.IsValid)
            {
                student.Id = nextId++;
                students.Add(student);
                return RedirectToAction("Index");
            }
            return View(student);
        }

        // UPDATE - GET
        public IActionResult Edit(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student == null) return NotFound();
            return View(student);
        }

        // UPDATE - POST
        [HttpPost]
        public IActionResult Edit(Student student)
        {
            if (ModelState.IsValid)
            {
                var existing = students.FirstOrDefault(s => s.Id == student.Id);
                if (existing != null)
                {
                    existing.Name = student.Name;
                    existing.Email = student.Email;
                    existing.Age = student.Age;
                }
                return RedirectToAction("Index");
            }
            return View(student);
        }

        // DELETE - GET
        public IActionResult Delete(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student == null) return NotFound();
            return View(student);
        }

        // DELETE - POST
        [HttpPost, ActionName("Delete")]
        public IActionResult DeleteConfirmed(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student != null)
            {
                students.Remove(student);
            }
            return RedirectToAction("Index");
        }
    }
}