using AutoMapper;
using ass9.Models;
using ass9.DTOs;

namespace ass9.Profiles
{
    public class StudentProfile : Profile
    {
        public StudentProfile()
        {
            // Entity → DTO
            CreateMap<Student, StudentDto>();

            // DTO → Entity
            CreateMap<CreateStudentDto, Student>();
        }
    }
}