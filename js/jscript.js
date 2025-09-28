// Manejo de navegación entre secciones
document.addEventListener("DOMContentLoaded", () => {
  const navLinks = document.querySelectorAll(".sidebar .nav-link");
  const sections = document.querySelectorAll(".section");

  navLinks.forEach(link => {
    link.addEventListener("click", e => {
      e.preventDefault();

      // Remover active de links
      navLinks.forEach(l => l.classList.remove("active"));
      link.classList.add("active");

      // Mostrar sección correspondiente
      const target = link.getAttribute("data-target");
      sections.forEach(sec => {
        sec.classList.remove("active");
        if (sec.id === target) {
          sec.classList.add("active");
        }
      });
    });
  });
});
