# Tvt22spl_syksy2023_projekti

Käyttäen nRF5340 Development Kittiä mittaamme kiihtyvyysanturin dataa ja välitämme tiedon langattomasti Raspberry Pi:lle. Raspberry välittää dataa Oamkin MySQL-palvelimelle.

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja yksinkertainen HTTP API. Kerättyä dataa haetaan HTTP-rajapinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään koneoppimistarkoituksiin.
