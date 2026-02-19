using Microsoft.AspNetCore.Mvc;

namespace ass4.Controllers
{
    public class HomeController : Controller
    {
        private readonly IConfiguration _configuration;

        public HomeController(IConfiguration configuration)
        {
            _configuration = configuration;
        }

        public IActionResult Index()
        {
            var appName = _configuration["MySettings:AppName"];
            var version = _configuration["MySettings:Version"];

            ViewBag.AppName = appName;
            ViewBag.Version = version;

            return View();
        }
    }
}