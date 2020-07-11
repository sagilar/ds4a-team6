using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Ds4At6.Api.Models;

namespace Ds4At6.Api.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CrimesController : ControllerBase
    {
        private readonly DataContext _context;

        public CrimesController(DataContext context)
        {
            _context = context;
        }

        // GET: api/Crimes
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Crime>>> GetCrime()
        {
            return await _context.Crime.ToListAsync();
        }

        // GET: api/Crimes/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Crime>> GetCrime(int id)
        {
            var crime = await _context.Crime.FindAsync(id);

            if (crime == null)
            {
                return NotFound();
            }

            return crime;
        }

        // PUT: api/Crimes/5
        // To protect from overposting attacks, enable the specific properties you want to bind to, for
        // more details, see https://go.microsoft.com/fwlink/?linkid=2123754.
        [HttpPut("{id}")]
        public async Task<IActionResult> PutCrime(int id, Crime crime)
        {
            if (id != crime.CrimeId)
            {
                return BadRequest();
            }

            _context.Entry(crime).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!CrimeExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Crimes
        // To protect from overposting attacks, enable the specific properties you want to bind to, for
        // more details, see https://go.microsoft.com/fwlink/?linkid=2123754.
        [HttpPost]
        public async Task<ActionResult<Crime>> PostCrime(Crime crime)
        {
            _context.Crime.Add(crime);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetCrime", new { id = crime.CrimeId }, crime);
        }

        // DELETE: api/Crimes/5
        [HttpDelete("{id}")]
        public async Task<ActionResult<Crime>> DeleteCrime(int id)
        {
            var crime = await _context.Crime.FindAsync(id);
            if (crime == null)
            {
                return NotFound();
            }

            _context.Crime.Remove(crime);
            await _context.SaveChangesAsync();

            return crime;
        }

        private bool CrimeExists(int id)
        {
            return _context.Crime.Any(e => e.CrimeId == id);
        }
    }
}
