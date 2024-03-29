<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Redovalnica</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.2/css/bulma.min.css">
  <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
</head>

<body>
  <section class="hero is-small">
    <div class="hero-body">
      <p class="title">
        Redovalnica
      </p>
      <p class="subtitle">
          <nav class="right">
    <div class="level-right">
        <a class="button is-primary" href="/prijava/">
          <strong>Prijavi se</strong>
        </a>
        <form method="POST" action="/odjava/">
          <button class="button is-light">Odjavi se</button>
        </form>
    </div>
  </nav>
      </p>
    </div>
  </section>
  <section class="section">
    {{!base}}
  </section>
</body>

<footer class="footer">
  <div class="content has-text-centered">
    <p>
      <strong>Redovalnica</strong> by <a href="https://github.com/MajaKomic/Projektna-naloga-UVP">Maja Komic</a>.
    </p>
  </div>
</footer>

</html>