const themeToggle = document.getElementById('themeToggle');
const scrollTopBtn = document.getElementById('scrollTop');
const loading = document.getElementById('loading');
let isDarkMode = false;

// ===== LOADING SCREEN =====
window.addEventListener('load', () => {
  setTimeout(() => {
    loading.classList.add('hidden');
  }, 1500);
});

// ===== THEME TOGGLE =====
themeToggle.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
  isDarkMode = !isDarkMode;
  
  if (isDarkMode) {
    themeToggle.innerHTML = '☀️ Modo Claro';
  } else {
    themeToggle.innerHTML = '🌙 Modo Oscuro';
  }
});

// ===== TYPING EFFECT =====
function typeEffect(element, text, speed = 80) {
  element.innerHTML = '';
  let i = 0;
  
  function type() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(type, speed);
    }
  }
  type();
}

// Aplicar efecto de escritura
setTimeout(() => {
  const subtitle = document.querySelector('.subtitle');
  const originalText = subtitle.textContent;
  typeEffect(subtitle, originalText);
}, 2000);

// ===== SCROLL ANIMATIONS =====
function animateOnScroll() {
  const sections = document.querySelectorAll('section');
  
  sections.forEach(section => {
    const sectionTop = section.getBoundingClientRect().top;
    const triggerPoint = window.innerHeight - 100;
    
    if (sectionTop < triggerPoint) {
      section.classList.add('show');
    }
  });
}

// ===== SCROLL TO TOP BUTTON =====
window.addEventListener('scroll', () => {
  // Animate sections
  animateOnScroll();
  
  // Show/hide scroll button
  if (window.pageYOffset > 300) {
    scrollTopBtn.classList.add('show');
  } else {
    scrollTopBtn.classList.remove('show');
  }
});

scrollTopBtn.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});

// ===== INTERACTIVE EFFECTS =====

// Avatar click effect
const avatar = document.querySelector('.avatar');
avatar.addEventListener('click', () => {
  avatar.style.animation = 'none';
  setTimeout(() => {
    avatar.style.animation = 'spin 1s ease';
  }, 10);
});

// Skill items click effect
const skillItems = document.querySelectorAll('.skill-item');
skillItems.forEach(skill => {
  skill.addEventListener('click', () => {
    skill.style.transform = 'scale(1.1) rotate(5deg)';
    setTimeout(() => {
      skill.style.transform = '';
    }, 300);
  });
});

// Project cards click effect
const projectCards = document.querySelectorAll('.project-card');
projectCards.forEach(card => {
  card.addEventListener('click', () => {
    card.style.transform = 'translateY(-10px) rotate(-2deg) scale(1.05)';
    setTimeout(() => {
      card.style.transform = '';
    }, 400);
  });
});

// ===== CONTACT LINKS COPY TO CLIPBOARD =====
const contactLinks = document.querySelectorAll('.contact a');
contactLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();

    // Guardar el texto original
    const originalText = link.textContent.trim();

    // Copiar el texto original al portapapeles
    navigator.clipboard.writeText(originalText).then(() => {
      console.log(`Copiado: ${originalText}`);
    }).catch(err => {
      console.error('Error al copiar: ', err);
    });

    // Feedback sutil (cambio de color)
    link.style.color = '#27ae60';
    setTimeout(() => {
      link.style.color = '';
    }, 800);
  });
});

// ===== INITIAL ANIMATIONS =====
document.addEventListener('DOMContentLoaded', () => {
  // Initial scroll check
  animateOnScroll();
});

// ===== EASTER EGG =====
let clickCount = 0;
document.addEventListener('click', () => {
  clickCount++;
  if (clickCount === 10) {
    document.body.style.animation = 'rainbow 2s infinite';
    setTimeout(() => {
      document.body.style.animation = '';
      clickCount = 0;
    }, 4000);
  }
});

// Add rainbow animation
const style = document.createElement('style');
style.textContent = `
  @keyframes rainbow {
    0% { filter: hue-rotate(0deg); }
    25% { filter: hue-rotate(90deg); }
    50% { filter: hue-rotate(180deg); }
    75% { filter: hue-rotate(270deg); }
    100% { filter: hue-rotate(360deg); }
  }
`;
document.head.appendChild(style);

// ===== CONSOLE MESSAGE =====
console.log(`
¡Hola desde mi CV!
Soy estudiante pero me gusta experimentar
Código hecho con cariño por Rodger
¡Gracias por revisar mi trabajo!

Easter egg: Haz click 10 veces en cualquier lugar
`);

// ===== SIMPLE PERFORMANCE OPTIMIZATION =====
let scrollTimer;
window.addEventListener('scroll', () => {
  clearTimeout(scrollTimer);
  scrollTimer = setTimeout(() => {
    animateOnScroll();
  }, 10);
});
