
Descripción:
    - Esta API permite conseguir memes de forma gratis o generarlos con IA.

Solicitudes:
1. Templates:
    - Método: GET
    - Endpoint: https://justmeme.wtf/api/v1/templates
    - Params/Body: page, limit, category
    - Descripción: Provee una cantidad determinada de plantillas de memes con opción de categoría y página del directorio.
    - Status code: 200
    - Respuesta:
    {
    "success": true,
    "templates": [
        {
            "id": "expanding-brain",
            "name": "Expanding Brain",
            "slug": "expanding-brain",
            "url": "https://i.imgflip.com/1jwhww.jpg",
            "categories": [
                "expanding",
                "multi-panel",
                "trending",
                "comparison"
            ]
        },
        {
            "id": "buff-doge-vs-cheems",
            "name": "Buff Doge vs Cheems",
            "slug": "buff-doge-vs-cheems",
            "url": "https://i.imgflip.com/43a45p.png",
            "categories": [
                "animal",
                "comparison",
                "two-panel",
                "trending"
            ]
        }
    ],
    "total": 2302,
    "page": 3,
    "limit": 2
}

2. Search:
    - Método: GET
    - Endpoint: https://justmeme.wtf/api/v1/templates/search
    - Params/Body: q
    - Descripción: Búsqueda de memes utilizando algún término o keyword como parámetro para la búsqueda.
    - Status code: 200
    - Respuesta:
    {
    "success": true,
    "templates": [
        {
            "id": "trump-bill-signing",
            "name": "Trump Bill Signing",
            "slug": "trump-bill-signing",
            "url": "https://i.imgflip.com/4/1ii4oc.jpg",
            "categories": []
        },
        {
            "id": "40115543-donald-trump-approves",
            "name": "Donald trump approves",
            "slug": "40115543-donald-trump-approves",
            "url": "https://i.imgflip.com/4/nvtcn.jpg",
            "categories": []
        },
        {
            "id": "40314559-donald-trump",
            "name": "Donald Trump",
            "slug": "40314559-donald-trump",
            "url": "https://i.imgflip.com/4/o02wv.jpg",
            "categories": []
        },
        {
            "id": "556538140-trump-mcdonalds-drive-thru",
            "name": "Trump McDonald&#039;s Drive-thru",
            "slug": "556538140-trump-mcdonalds-drive-thru",
            "url": "https://i.imgflip.com/4/97cjks.jpg",
            "categories": []
        },
        {
            "id": "478458580-donald-trump-mugshot",
            "name": "Donald Trump Mugshot",
            "slug": "478458580-donald-trump-mugshot",
            "url": "https://i.imgflip.com/4/7wv104.jpg",
            "categories": []
        },
        {
            "id": "127200701-trumpet-boy",
            "name": "Trumpet Boy",
            "slug": "127200701-trumpet-boy",
            "url": "https://i.imgflip.com/4/23qcot.jpg",
            "categories": []
        },
        {
            "id": "40181531-donald-trump",
            "name": "Donald Trump",
            "slug": "40181531-donald-trump",
            "url": "https://i.imgflip.com/4/nx89n.jpg",
            "categories": []
        },
        {
            "id": "259542992-trump-interview",
            "name": "Trump interview",
            "slug": "259542992-trump-interview",
            "url": "https://i.imgflip.com/4/4aiwnk.jpg",
            "categories": []
        },
        {
            "id": "282746360-trump-dancing",
            "name": "trump dancing",
            "slug": "282746360-trump-dancing",
            "url": "https://i.imgflip.com/2/4oc8hk.jpg",
            "categories": []
        },
        {
            "id": "trump",
            "name": "Donald Trump",
            "slug": "trump",
            "url": "https://api.memegen.link/images/trump.jpg",
            "categories": []
        } 
    ],
    "total": 10
}

3. AI Generate:
    - Método: POST
    - Endpoint: https://justmeme.wtf/api/v1/ai-generate
    - Params/Body: prompt (de lo que debería tratar el meme)
    - Descripción: Genera un meme utilizando inteligencia artificial a partir de un prompt proveído.
    - Status code: 503 (AI service  temporarily unavailable)
    - Respuesta:
    {
    "success": false,
    "error": "AI service temporarily unavailable. Try again later."
}

¿Qué aprendiste del proceso?
    Aprendí lo que es un endpoint.
    Aprendí que no todos los APIs permiten probar todos los métodos HTTP, muchos solo permiten el método de POST.
