using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using AutoMapper;
using ass9.DTOs;
using ass9.Data;
using ass9.Models;

[ApiController]
[Route("api/v{version:apiVersion}/[controller]")]
[ApiVersion("1.0")]
public class StudentsController : ControllerBase
{
    private readonly ApplicationDbContext _context;
    private readonly IMapper _mapper;

    public StudentsController(ApplicationDbContext context, IMapper mapper)
    {
        _context = context;
        _mapper = mapper;
    }

    // GET: api/v1/students
    [HttpGet]
    public async Task<ActionResult<IEnumerable<StudentDto>>> GetStudents()
    {
        var students = await _context.Students.ToListAsync();
        return Ok(_mapper.Map<IEnumerable<StudentDto>>(students));
    }

    // GET: api/v1/students/1
    [HttpGet("{id}")]
    public async Task<ActionResult<StudentDto>> GetStudent(int id)
    {
        var student = await _context.Students.FindAsync(id);
        if (student == null)
            return NotFound();

        return Ok(_mapper.Map<StudentDto>(student));
    }

    // POST
    [HttpPost]
    public async Task<ActionResult<StudentDto>> CreateStudent(CreateStudentDto dto)
    {
var student = new Student
{
    Name = dto.Name,
    Email = dto.Email,
    Age = dto.Age
};        _context.Students.Add(student);
        await _context.SaveChangesAsync();

        var result = _mapper.Map<StudentDto>(student);

        return CreatedAtAction(nameof(GetStudent),
            new { id = student.Id },
            result);
    }

    // PUT
    [HttpPut("{id}")]
    public async Task<IActionResult> UpdateStudent(int id, CreateStudentDto dto)
    {
        var student = await _context.Students.FindAsync(id);
        if (student == null)
            return NotFound();

        _mapper.Map(dto, student);
        await _context.SaveChangesAsync();

        return NoContent();
    }

    // DELETE
    [HttpDelete("{id}")]
    public async Task<IActionResult> DeleteStudent(int id)
    {
        var student = await _context.Students.FindAsync(id);
        if (student == null)
            return NotFound();

        _context.Students.Remove(student);
        await _context.SaveChangesAsync();

        return NoContent();
    }
}