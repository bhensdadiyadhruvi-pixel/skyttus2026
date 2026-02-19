using Microsoft.AspNetCore.Mvc;
using MvcEfApp.Data;
using MvcEfApp.Models;
using System.Linq;

namespace MvcEfApp.Controllers
{
    public class StudentController : Controller
    {
        private readonly ApplicationDbContext _context;

        public StudentController(ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            var students = _context.Students.ToList(); // LINQ query
            return View(students);
        }
    }
}