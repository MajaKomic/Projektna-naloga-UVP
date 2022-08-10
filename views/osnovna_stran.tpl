% rebase('osnova.tpl')
<!-- Main container -->
<nav class="level">
    <div class="level-left">
        <div class="buttons has-addons field is-horizontal">
            % for id_semestra, semester in enumerate(semestri):
            <a href="/semester/{{id_semestra}}/" class="button" name="id_semestra" value="{{id_semestra}}">
                {{semester.ime_semestra}}
            </a>
            % end
        </div>

    </div>

    <div class="level-right">
            <div class="level-item">
                <a class="button is-info" href="/dodaj-semester/">dodaj semester</a>
            </div>
        </form>
    </div>
</nav>