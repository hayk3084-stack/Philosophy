PHILOSOPHERS = [
    {
        "name": "René Descartes",
        "country": "France",
        "birth_year": 1596,
        "death_year": 1650,
        "school": "Rationalism",
        "catch_phrase": "I think therefore I am",
    },
    {
        "name": "David Hume",
        "country": "Scotland",
        "birth_year": 1711,
        "death_year": 1776,
        "school": "Empiricism",
        "catch_phrase": "Reason is, and ought only to be, the slave of the passions",
    },
]

WRITINGS = [
    {
        "title": "Meditations",
        "kind": "book",
        "publish_year": 1641,
        "philosopher": "René Descartes",
    },
]

ARGUMENTS = [
    {
        "name": "Senses argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "Descartes' first argument for doubt rests on the unreliability of the senses. Everything he had accepted as most true came to him through the senses, yet the senses have sometimes deceived him. Since it is unwise to fully trust anything that has deceived us even once, he concludes that beliefs based on the senses cannot be accepted as certain.",
    },
    {
        "name": "Dream argument",
        "writing": "Meditations",
        "philosopher": "René Descartes",
        "description": "The dream argument pushes the doubt further. Even if the senses sometimes deceive us about distant or small things, it seems certain that I am sitting here by the fire, holding this paper. Yet he recalls that in dreams he has been just as convinced of such things while actually lying in bed. Since there are no certain signs by which waking can be distinguished from dreaming, he cannot be sure he is not dreaming right now, and so even his most immediate sensory experiences cannot be accepted as certain.",
    },
]

CONNECTIONS = [
    {
        "source_arg": "Dream argument",
        "relation_type": "based_on",
        "target_arg": "Senses argument",
    },
]