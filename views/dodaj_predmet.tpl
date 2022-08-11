% rebase('osnova.tpl')
<table class="table is-hoverable is-fullwidth">
    <thead>
        <tr>
            <form method="POST" action="/dodaj-predmet/{{id_semestra}}/">
                <td></td>
                <tr>
                    <td>
                        <div class="control has-icons-left">
                            <input class="input is-small" type="text" name="ime_predmeta" placeholder="ime predmeta">
                            <span class="icon is-small is-left">
                                <i class="far fa-clipboard-check"></i>
                            </span>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>
                        <div class="control has-icons-left">
                            <input class="input is-small" type="text" name="predavatelj" placeholder="ime predavatelja">
                            <span class="icon is-small is-left">
                                <i class="far fa-clipboard-check"></i>
                            </span>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>
                        <div class="control has-icons-left">
                            <input class="input is-small" type="text" name="asistent" placeholder="ime asistenta">
                            <span class="icon is-small is-left">
                                <i class="far fa-clipboard-check"></i>
                            </span>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>
                        <div class="control has-icons-left">
                            <input class="input is-small" type="text" name="kreditne_tocke" placeholder="stevilo kreditnih točk">
                            <span class="icon is-small is-left">
                                <i class="far fa-clipboard-check"></i>
                            </span>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>
                        <div class="control has-icons-left">
                            <input class="input is-small" type="text" name="ocena_vaj" placeholder="ocena iz vaj">
                            <span class="icon is-small is-left">
                                <i class="far fa-clipboard-check"></i>
                            </span>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>
                        <div class="control has-icons-left">
                            <input class="input is-small" type="text" name="ocena_teo" placeholder="ocena iz teorije">
                            <span class="icon is-small is-left">
                                <i class="far fa-clipboard-check"></i>
                            </span>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>
                        <div class="field is-grouped">
                            <div class="control">
                                <button class="button is-link">Dodaj</button>
                            </div>
                            <div class="control">
                                <a class="button is-link is-light" href="/">Prekliči</a>
                            </div>
                        </div>
                    </td>
                <tr>
            </form>
        </tr>
    </thead>
</table>