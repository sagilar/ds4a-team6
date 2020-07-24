using Ds4At6.Api.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Ds4At6.Api.Controllers
{
    [Route("api/{countryId}/regions")]
    [ApiController]
    public class RegionsController : ControllerBase
    {
        private readonly DataContext _context;

        public RegionsController(DataContext context)
        {
            _context = context;
        }

        // GET: api/Regions
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Region>>> GetRegions(int countryId)
        {
            return await _context.Region
                .Where(s => s.CountryId == countryId)
                .OrderBy(s => s.Name)
                .ToListAsync();
        }

        // GET: api/Regions/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Region>> GetRegion(int id)
        {
            var region = await _context.Region.FindAsync(id);

            if (region == null)
            {
                return NotFound();
            }

            return region;
        }

    }
}
