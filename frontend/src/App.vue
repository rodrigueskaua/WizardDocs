<template>
  <div class="min-vh-100 d-flex flex-column bg-light text-dark">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary px-4">
      <a class="navbar-brand" href="#">Wizard Docs</a>
    </nav>

    <main class="container flex-grow-1 py-4">
      <router-view />
    </main>

    <footer class="bg-primary text-white text-center py-3 mt-auto">
      &copy; 2025 Wizard Docs. Todos os direitos reservados.
    </footer>
  </div>
</template>