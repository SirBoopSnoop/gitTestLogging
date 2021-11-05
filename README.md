# gitTestLogging

Lastet opp filene fra oblig 2 i nytt repository og navigerte deretter til "Actions" menyen i GitHub. GitHub kjente igjen Python som programmeringsspråket mitt, og lot meg velge
mellom mange forskjellige "workflows". Jeg valgte "python application", som gir meg ferdig-generert eksempelkode på handlinger som skal utføres hver gang det skjer en pull- eller
push-request. Siste av disse handlingene er å teste med pytest. Når jeg da "commit-et" workflowen direkte til main, vil denne kodesnutten kjøre hver gang jeg jeg gjør en push/pull
request. Første commit fungerte ikke for meg, siden applikasjonen ikke kjente igjen et av punktene i requirements.txt, men etter jeg endret på den fikk jeg gjort en pull request 
og committet med 4 godkjente tester.
