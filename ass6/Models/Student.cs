using System.ComponentModel.DataAnnotations;

namespace MvcCrudApp.Models
{
    public class Student
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "Name is required")]
        [StringLength(50)]
        public string Name { get; set; }

        [Required(ErrorMessage = "Email is required")]
        [EmailAddress(ErrorMessage = "Invalid Email")]
        public string Email { get; set; }

        [Range(18, 30, ErrorMessage = "Age must be between 18 and 30")]
        public int Age { get; set; }
    }
}