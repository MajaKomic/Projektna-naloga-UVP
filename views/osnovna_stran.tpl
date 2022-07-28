<h1>Dobrodošli</h1>

<h2>Tukaj je seznam semestrov:</h2>
<ul>
% for semester in semestri:
    <li>
        {{ semester.ime_semestra}}
        % for predmet in semester.predmeti:
            <li>
                {{ predmet.ime_predmeta}}
            <\li>
    </li>
</ul>