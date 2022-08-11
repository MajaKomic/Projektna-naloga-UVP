% rebase('osnova.tpl')
<!-- Main container -->
<nav class="level">
    <div class="level-left">
        <div class="buttons has-addons field is-horizontal">
            % for id_semestra, semester in enumerate(semestri):
            % if semester == aktualni_semester:
            <a class="button is-primary is-selected" name="id_semestra" value="{{id_semestra}}">
                {{semester.ime_semestra}}
            </a>
            % else:
            <a href="/semester/{{id_semestra}}/" class="button" name="id_semestra" value="{{id_semestra}}">
                {{semester.ime_semestra}}
            </a>
            % end
            % end
        </div>
    </div>

    <div class="level-right">
        <!-- <div class="level-item">
            <p class="subtitle is-5">
                <strong>123</strong> posts
            </p>
        </div> -->
            <div class="level-item">
                <a class="button is-info" href="/dodaj-semester/">dodaj semester</a>
            </div>
        </form>
    </div>
</nav>


% if aktualni_semester:

<div class="level-left">
        <div class="level-item">
                <td></td>
            <a class="button is-info" href="/dodaj-predmet/{{id_aktualni_semester}}/">dodaj predmet</a>
        </div>
    </form>
</div>

<table class="table is-hoverable is-fullwidth">
    <thead>    
        <tr>
            <td></td>
            <td><strong>Predmet</strong></td>
            <td><strong>Predavatelj</strong></td>
            <td><strong>Asistent</strong></td>
            <td><strong>Kreditne točke</strong></td>
            <td><strong>Ocena vaj</strong></td>
            <td><strong>Ocena teorije</strong></td>
        </tr>
    </thead>
    <tbody>
        % for id_predmeta, predmet in enumerate(aktualni_semester.predmeti):
            <tr>
                <td>
                <form method="POST" action="/pobrisi-predmet/{{id_aktualni_semester}}/{{id_predmeta}}/">
                    <button class="button is-danger is-light">X</button>
                </form>
                </td>
                <td>{{ predmet.ime_predmeta }}</td>
                <td>{{ predmet.predavatelj }}</td>
                <td>{{ predmet.asistent }}</td>
                <td>{{ predmet.kreditne_tocke }}</td>
                <td>{{ predmet.ocena_vaj }}</td>
                <td>{{ predmet.ocena_teo }}</td>
                <td></td>
            </tr>
        % end
    </tbody>
</table>

% else:

<p>Nimate še nobenega semestra. <a href="/dodaj-semester/">Dodajte ga!</a></p>