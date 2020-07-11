using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class Regional
    {
        public Regional()
        {
            Prison = new HashSet<Prison>();
        }

        public int RegionalId { get; set; }
        public string Name { get; set; }

        public virtual ICollection<Prison> Prison { get; set; }
    }
}
