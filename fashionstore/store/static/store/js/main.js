// Auto-dismiss messages after 4 seconds
document.addEventListener('DOMContentLoaded', () => {
  const messages = document.querySelectorAll('.message');
  messages.forEach(msg => {
    setTimeout(() => {
      msg.style.transition = 'opacity .5s ease';
      msg.style.opacity = '0';
      setTimeout(() => msg.remove(), 500);
    }, 4000);
  });
});
