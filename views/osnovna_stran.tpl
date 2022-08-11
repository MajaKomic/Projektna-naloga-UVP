% rebase('osnova.tpl')
<!-- Main container -->

<div><strong>Pozdravljeni, tukaj je seznam vaših semestrov:</strong></div>

<table class="table is-hoverable">
    % for id_semestra, semester in enumerate(semestri):
    <tr>
        <td>
            <a href="/semester/{{id_semestra}}/" class="button is-primary" name="id_semestra" value="{{id_semestra}}">
                {{semester.ime_semestra}}
            </a>
        </td>
        <td>
            <form method="POST" action="/pobrisi-semester/{{id_semestra}}/">
                <button class="button is-danger is-light">X</button>
            </form>
        </td>
    </tr>
    % end
</table>

<div></div>

<div class="level-left">
        <div class="level-item">
            <a class="button is-info" href="/dodaj-semester/">dodaj semester</a>
        </div>
    </form>
</div>