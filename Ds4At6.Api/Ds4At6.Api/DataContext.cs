using Microsoft.EntityFrameworkCore;

namespace Ds4At6.Api.Models
{
    public partial class DataContext : DbContext
    {
        public DataContext()
        {
        }

        public DataContext(DbContextOptions<DataContext> options)
            : base(options)
        {
        }

        public virtual DbSet<CitiesView> CitiesView { get; set; }
        public virtual DbSet<City> City { get; set; }
        public virtual DbSet<Country> Country { get; set; }
        public virtual DbSet<Crime> Crime { get; set; }
        public virtual DbSet<CrimeGroup> CrimeGroup { get; set; }
        public virtual DbSet<Gender> Gender { get; set; }
        public virtual DbSet<MaritalStatus> MaritalStatus { get; set; }
        public virtual DbSet<Person> Person { get; set; }
        public virtual DbSet<PersonCondition> PersonCondition { get; set; }
        public virtual DbSet<Prison> Prison { get; set; }
        public virtual DbSet<Reclusion> Reclusion { get; set; }
        public virtual DbSet<ReclusionStatus> ReclusionStatus { get; set; }
        public virtual DbSet<Region> Region { get; set; }
        public virtual DbSet<Regional> Regional { get; set; }
        public virtual DbSet<RegionsView> RegionsView { get; set; }
        public virtual DbSet<Scholarship> Scholarship { get; set; }
        public virtual DbSet<SpecialCondition> SpecialCondition { get; set; }
        public virtual DbSet<Staging> Staging { get; set; }
        public virtual DbSet<StatusLog> StatusLog { get; set; }
        public virtual DbSet<TempPospenados> TempPospenados { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<CitiesView>(entity =>
            {
                entity.HasNoKey();

                entity.ToView("CitiesView");

                entity.Property(e => e.CityName)
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.CountryName)
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.RegionName)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<City>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.HasOne(d => d.Region)
                    .WithMany(p => p.City)
                    .HasForeignKey(d => d.RegionId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_City_Region");
            });

            modelBuilder.Entity<Country>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Crime>(entity =>
            {
                entity.Property(e => e.Name)
                    .IsRequired()
                    .HasMaxLength(200)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<CrimeGroup>(entity =>
            {
                entity.HasKey(e => e.GroupId)
                    .HasName("PK__CrimeGro__149AF36A5C86FC4B");

                entity.Property(e => e.Group)
                    .IsRequired()
                    .HasMaxLength(200)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Gender>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(20)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<MaritalStatus>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(20)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Person>(entity =>
            {
                entity.HasIndex(e => e.RemoteId)
                    .HasName("UQ__Person__9EFEB0C517FB1AE5")
                    .IsUnique();

                entity.Property(e => e.AdultoMayor).HasColumnName("ADULTO MAYOR");

                entity.Property(e => e.AfroColombiano).HasColumnName("AFRO COLOMBIANO");

                entity.Property(e => e.Bisexual).HasColumnName("BISEXUAL");

                entity.Property(e => e.ConDiscapacidad).HasColumnName("CON DISCAPACIDAD");

                entity.Property(e => e.Extranjeros).HasColumnName("EXTRANJEROS");

                entity.Property(e => e.Gays).HasColumnName("GAYS");

                entity.Property(e => e.HasKids)
                    .HasMaxLength(2)
                    .IsUnicode(false);

                entity.Property(e => e.Indigena).HasColumnName("INDIGENA");

                entity.Property(e => e.Intersexual).HasColumnName("INTERSEXUAL");

                entity.Property(e => e.Lesbiana).HasColumnName("LESBIANA");

                entity.Property(e => e.MadreGestante).HasColumnName("MADRE GESTANTE");

                entity.Property(e => e.MadreLactante).HasColumnName("MADRE LACTANTE");

                entity.Property(e => e.Raizales).HasColumnName("RAIZALES");

                entity.Property(e => e.RemoteId)
                    .IsRequired()
                    .HasMaxLength(40)
                    .IsUnicode(false);

                entity.Property(e => e.Rom).HasColumnName("ROM");

                entity.Property(e => e.Transexual).HasColumnName("TRANSEXUAL");

                entity.HasOne(d => d.City)
                    .WithMany(p => p.Person)
                    .HasForeignKey(d => d.CityId)
                    .HasConstraintName("FK_Person_City");

                entity.HasOne(d => d.Gender)
                    .WithMany(p => p.Person)
                    .HasForeignKey(d => d.GenderId)
                    .HasConstraintName("FK_Person_Gender");

                entity.HasOne(d => d.MaritalStatus)
                    .WithMany(p => p.Person)
                    .HasForeignKey(d => d.MaritalStatusId)
                    .HasConstraintName("FK_Person_MaritalStatus");

                entity.HasOne(d => d.Scholarship)
                    .WithMany(p => p.Person)
                    .HasForeignKey(d => d.ScholarshipId)
                    .HasConstraintName("FK_Person_Scholarship");
            });

            modelBuilder.Entity<PersonCondition>(entity =>
            {
                entity.HasOne(d => d.Person)
                    .WithMany(p => p.PersonCondition)
                    .HasForeignKey(d => d.PersonId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_PersonCondition_Person");

                entity.HasOne(d => d.SpecialCondition)
                    .WithMany(p => p.PersonCondition)
                    .HasForeignKey(d => d.SpecialConditionId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_PersonCondition_SpecialCondition");
            });

            modelBuilder.Entity<Prison>(entity =>
            {
                entity.Property(e => e.Name)
                    .IsRequired()
                    .HasMaxLength(180)
                    .IsUnicode(false);

                entity.HasOne(d => d.City)
                    .WithMany(p => p.Prison)
                    .HasForeignKey(d => d.CityId)
                    .HasConstraintName("FK_ReclusionSite_City");

                entity.HasOne(d => d.Regional)
                    .WithMany(p => p.Prison)
                    .HasForeignKey(d => d.RegionalId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_ReclusionSite_Regional");
            });

            modelBuilder.Entity<Reclusion>(entity =>
            {
                entity.HasNoKey();

                entity.HasIndex(e => e.PersonId)
                    .HasName("IX_PersonId");

                entity.Property(e => e.CaptureDate).HasColumnType("date");

                entity.Property(e => e.EndDate).HasColumnType("date");

                entity.Property(e => e.ReclusionId).ValueGeneratedOnAdd();

                entity.Property(e => e.StartDate).HasColumnType("date");

                entity.HasOne(d => d.Crime)
                    .WithMany()
                    .HasForeignKey(d => d.CrimeId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_Reclusion_Crime");

                entity.HasOne(d => d.Person)
                    .WithMany()
                    .HasForeignKey(d => d.PersonId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_Reclusion_Person");

                entity.HasOne(d => d.Prison)
                    .WithMany()
                    .HasForeignKey(d => d.PrisonId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_Reclusion_ReclusionSite");

                entity.HasOne(d => d.ReclusionStatus)
                    .WithMany()
                    .HasForeignKey(d => d.ReclusionStatusId)
                    .HasConstraintName("FK_Reclusion_ReclusionStatus");
            });

            modelBuilder.Entity<ReclusionStatus>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Region>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.HasOne(d => d.Country)
                    .WithMany(p => p.Region)
                    .HasForeignKey(d => d.CountryId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_Region_Country");
            });

            modelBuilder.Entity<Regional>(entity =>
            {
                entity.Property(e => e.Name)
                    .IsRequired()
                    .HasMaxLength(50)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<RegionsView>(entity =>
            {
                entity.HasNoKey();

                entity.ToView("RegionsView");

                entity.Property(e => e.CountryName)
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.RegionName)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Scholarship>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<SpecialCondition>(entity =>
            {
                entity.Property(e => e.Condition)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Staging>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("staging");

                entity.Property(e => e.ActividadesEnseñanza)
                    .HasColumnName("ACTIVIDADES_ENSEÑANZA")
                    .HasMaxLength(255);

                entity.Property(e => e.ActividadesEstudio)
                    .HasColumnName("ACTIVIDADES_ESTUDIO")
                    .HasMaxLength(255);

                entity.Property(e => e.ActividadesTrabajo)
                    .HasColumnName("ACTIVIDADES_TRABAJO")
                    .HasMaxLength(255);

                entity.Property(e => e.Agravado)
                    .HasColumnName("AGRAVADO")
                    .HasMaxLength(255);

                entity.Property(e => e.AnoNacimiento)
                    .HasColumnName("ANO_NACIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.Calificado)
                    .HasColumnName("CALIFICADO")
                    .HasMaxLength(255);

                entity.Property(e => e.Ciudad)
                    .HasColumnName("CIUDAD")
                    .HasMaxLength(255);

                entity.Property(e => e.CodigoEstablecimiento)
                    .HasColumnName("CODIGO_ESTABLECIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.CondicExpecional)
                    .HasColumnName("CONDIC_EXPECIONAL")
                    .HasMaxLength(255);

                entity.Property(e => e.Delito)
                    .HasColumnName("DELITO")
                    .HasMaxLength(255);

                entity.Property(e => e.Departamento)
                    .HasColumnName("DEPARTAMENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.DeptoEstablecimiento)
                    .HasColumnName("DEPTO_ESTABLECIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.Edad).HasColumnName("EDAD");

                entity.Property(e => e.Establecimiento)
                    .HasColumnName("ESTABLECIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.Estado)
                    .HasColumnName("ESTADO")
                    .HasMaxLength(255);

                entity.Property(e => e.EstadoCivil)
                    .HasColumnName("ESTADO_CIVIL")
                    .HasMaxLength(255);

                entity.Property(e => e.EstadoIngreso)
                    .HasColumnName("ESTADO_INGRESO")
                    .HasMaxLength(255);

                entity.Property(e => e.FechaCaptura)
                    .HasColumnName("FECHA_CAPTURA")
                    .HasMaxLength(255);

                entity.Property(e => e.FechaIngreso)
                    .HasColumnName("FECHA_INGRESO")
                    .HasMaxLength(255);

                entity.Property(e => e.FechaSalida)
                    .HasColumnName("FECHA_SALIDA")
                    .HasMaxLength(255);

                entity.Property(e => e.Genero)
                    .HasColumnName("GENERO")
                    .HasMaxLength(255);

                entity.Property(e => e.HijosMenores)
                    .HasColumnName("HIJOS_MENORES")
                    .HasMaxLength(255);

                entity.Property(e => e.Internoen)
                    .HasColumnName("INTERNOEN")
                    .HasMaxLength(255);

                entity.Property(e => e.MpioEstablecimiento)
                    .HasColumnName("MPIO_ESTABLECIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.NivelEducativo)
                    .HasColumnName("NIVEL_EDUCATIVO")
                    .HasMaxLength(255);

                entity.Property(e => e.PaisInterno)
                    .HasColumnName("PAIS_INTERNO")
                    .HasMaxLength(255);

                entity.Property(e => e.Regional)
                    .HasColumnName("REGIONAL")
                    .HasMaxLength(255);

                entity.Property(e => e.Reincidente)
                    .HasColumnName("REINCIDENTE")
                    .HasMaxLength(255);

                entity.Property(e => e.SituacionJuridica)
                    .HasColumnName("SITUACION_JURIDICA")
                    .HasMaxLength(255);

                entity.Property(e => e.SubtituloDelito)
                    .HasColumnName("SUBTITULO_DELITO")
                    .HasMaxLength(200)
                    .IsUnicode(false);

                entity.Property(e => e.Tentativa)
                    .HasColumnName("TENTATIVA")
                    .HasMaxLength(255);

                entity.Property(e => e.TituloDelito)
                    .HasColumnName("TITULO_DELITO")
                    .HasMaxLength(200)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<StatusLog>(entity =>
            {
                entity.Property(e => e.ProcDate).HasColumnType("smalldatetime");
            });

            modelBuilder.Entity<TempPospenados>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("temp_pospenados");

                entity.Property(e => e.ActividadesEnseñanza)
                    .HasColumnName("ACTIVIDADES_ENSEÑANZA")
                    .HasMaxLength(255);

                entity.Property(e => e.ActividadesEstudio)
                    .HasColumnName("ACTIVIDADES_ESTUDIO")
                    .HasMaxLength(255);

                entity.Property(e => e.ActividadesTrabajo)
                    .HasColumnName("ACTIVIDADES_TRABAJO")
                    .HasMaxLength(255);

                entity.Property(e => e.Agravado)
                    .HasColumnName("AGRAVADO")
                    .HasMaxLength(255);

                entity.Property(e => e.AnoNacimiento)
                    .HasColumnName("ANO_NACIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.Calificado)
                    .HasColumnName("CALIFICADO")
                    .HasMaxLength(255);

                entity.Property(e => e.Ciudad)
                    .HasColumnName("CIUDAD")
                    .HasMaxLength(255);

                entity.Property(e => e.CodigoEstablecimiento)
                    .HasColumnName("CODIGO_ESTABLECIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.CondicExpecional)
                    .HasColumnName("CONDIC_EXPECIONAL")
                    .HasMaxLength(255);

                entity.Property(e => e.Delito)
                    .HasColumnName("DELITO")
                    .HasMaxLength(255);

                entity.Property(e => e.Departamento)
                    .HasColumnName("DEPARTAMENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.DeptoEstablecimiento)
                    .HasColumnName("DEPTO_ESTABLECIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.Edad).HasColumnName("EDAD");

                entity.Property(e => e.Establecimiento)
                    .HasColumnName("ESTABLECIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.Estado)
                    .HasColumnName("ESTADO")
                    .HasMaxLength(255);

                entity.Property(e => e.EstadoCivil)
                    .HasColumnName("ESTADO_CIVIL")
                    .HasMaxLength(255);

                entity.Property(e => e.EstadoIngreso)
                    .HasColumnName("ESTADO_INGRESO")
                    .HasMaxLength(255);

                entity.Property(e => e.FechaCaptura)
                    .HasColumnName("FECHA_CAPTURA")
                    .HasMaxLength(255);

                entity.Property(e => e.FechaIngreso)
                    .HasColumnName("FECHA_INGRESO")
                    .HasMaxLength(255);

                entity.Property(e => e.FechaSalida)
                    .HasColumnName("FECHA_SALIDA")
                    .HasMaxLength(255);

                entity.Property(e => e.Genero)
                    .HasColumnName("GENERO")
                    .HasMaxLength(255);

                entity.Property(e => e.HijosMenores)
                    .HasColumnName("HIJOS_MENORES")
                    .HasMaxLength(255);

                entity.Property(e => e.Internoen)
                    .HasColumnName("INTERNOEN")
                    .HasMaxLength(255);

                entity.Property(e => e.MpioEstablecimiento)
                    .HasColumnName("MPIO_ESTABLECIMIENTO")
                    .HasMaxLength(255);

                entity.Property(e => e.NivelEducativo)
                    .HasColumnName("NIVEL_EDUCATIVO")
                    .HasMaxLength(255);

                entity.Property(e => e.PaisInterno)
                    .HasColumnName("PAIS_INTERNO")
                    .HasMaxLength(255);

                entity.Property(e => e.Regional)
                    .HasColumnName("REGIONAL")
                    .HasMaxLength(255);

                entity.Property(e => e.Reincidente)
                    .HasColumnName("REINCIDENTE")
                    .HasMaxLength(255);

                entity.Property(e => e.SituacionJuridica)
                    .HasColumnName("SITUACION_JURIDICA")
                    .HasMaxLength(255);

                entity.Property(e => e.SubtituloDelito)
                    .HasColumnName("SUBTITULO_DELITO")
                    .HasMaxLength(200)
                    .IsUnicode(false);

                entity.Property(e => e.Tentativa)
                    .HasColumnName("TENTATIVA")
                    .HasMaxLength(255);

                entity.Property(e => e.TituloDelito)
                    .HasColumnName("TITULO_DELITO")
                    .HasMaxLength(200)
                    .IsUnicode(false);
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
