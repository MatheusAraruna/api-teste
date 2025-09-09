from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/json')
def get_json():
    data = {
  "alerts": [
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 5,
      "reportByMunicipalityUser": "False",
      "confidence": 4,
      "reliability": 10,
      "type": "ROAD_CLOSED",
      "uuid": "ffb58346-b212-427c-b4e8-994d033796bd",
      "roadType": 1,
      "magvar": 172,
      "subtype": "ROAD_CLOSED_EVENT",
      "reportDescription": "",
      "location": {
        "x": -46.578823,
        "y": -23.628421
      },
      "pubMillis": 1755264119000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 2,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "HAZARD",
      "uuid": "42736d96-2ae7-4c82-9f28-69d4db5476e9",
      "roadType": 1,
      "magvar": 185,
      "subtype": "HAZARD_ON_ROAD",
      "street": "R. Major Carlos Del Prete",
      "location": {
        "x": -46.576392,
        "y": -23.613492
      },
      "pubMillis": 1757417648000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 3,
      "reportByMunicipalityUser": "False",
      "confidence": 5,
      "reliability": 10,
      "type": "HAZARD",
      "uuid": "aa00bdca-f184-430a-947c-25fc0b5135fd",
      "roadType": 2,
      "magvar": 352,
      "subtype": "HAZARD_ON_ROAD_POT_HOLE",
      "street": "Av. Guido Aliberti",
      "location": {
        "x": -46.575471,
        "y": -23.648527
      },
      "pubMillis": 1757111562000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 1,
      "reportByMunicipalityUser": "False",
      "confidence": 1,
      "reliability": 8,
      "type": "HAZARD",
      "uuid": "8bb9a36d-129d-4ba5-aa84-b5e72a41b326",
      "roadType": 2,
      "magvar": 47,
      "subtype": "HAZARD_ON_ROAD_POT_HOLE",
      "street": "Av. Guido Aliberti",
      "location": {
        "x": -46.572584,
        "y": -23.650095
      },
      "pubMillis": 1757354917000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 0,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "HAZARD",
      "uuid": "8c032643-5511-43d0-b4ff-6fc878736c29",
      "roadType": 2,
      "magvar": 323,
      "subtype": "HAZARD_ON_ROAD_CONSTRUCTION",
      "street": "Av. Guido Aliberti",
      "location": {
        "x": -46.574792,
        "y": -23.649468
      },
      "pubMillis": 1757415730000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 5,
      "reportByMunicipalityUser": "False",
      "confidence": 2,
      "reliability": 10,
      "type": "ROAD_CLOSED",
      "uuid": "80e88c83-a403-4dd8-bbaf-e26fb9657a27",
      "roadType": 2,
      "magvar": 292,
      "subtype": "ROAD_CLOSED_EVENT",
      "street": "Av. Fernando Simonsen",
      "reportDescription": "",
      "location": {
        "x": -46.569304,
        "y": -23.63246
      },
      "pubMillis": 1755264542000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 0,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "JAM",
      "uuid": "f887f837-6e7b-4e38-ab7d-c9cd285ebbfb",
      "roadType": 2,
      "magvar": 2,
      "subtype": "",
      "street": "Av. Sen. Roberto Simonsen",
      "location": {
        "x": -46.575313,
        "y": -23.622418
      },
      "pubMillis": 1757417914000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 1,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 6,
      "type": "JAM",
      "uuid": "5270dba9-239c-47d7-be02-7de9019c25c5",
      "roadType": 2,
      "magvar": 341,
      "subtype": "JAM_STAND_STILL_TRAFFIC",
      "street": "Av. Pres. Kennedy",
      "location": {
        "x": -46.558928,
        "y": -23.639788
      },
      "pubMillis": 1757417387000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 2,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "HAZARD",
      "uuid": "5d2cf2d6-edc3-48be-9891-12610dfc7217",
      "roadType": 2,
      "magvar": 359,
      "subtype": "HAZARD_ON_SHOULDER_CAR_STOPPED",
      "street": "R. Amazonas",
      "location": {
        "x": -46.569391,
        "y": -23.623636
      },
      "pubMillis": 1757416980000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 5,
      "reportByMunicipalityUser": "False",
      "confidence": 2,
      "reliability": 10,
      "type": "ROAD_CLOSED",
      "uuid": "07f85a68-3644-453b-b621-3f85cf030cbd",
      "roadType": 2,
      "magvar": 120,
      "subtype": "ROAD_CLOSED_EVENT",
      "street": "Av. Nelson Braido",
      "reportDescription": "",
      "location": {
        "x": -46.58014,
        "y": -23.62799
      },
      "pubMillis": 1755264428000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 5,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 7,
      "type": "ROAD_CLOSED",
      "uuid": "7b3b485e-d62e-42ed-8eef-b3a2b4d603de",
      "roadType": 2,
      "magvar": 117,
      "subtype": "ROAD_CLOSED_EVENT",
      "street": "Av. Nelson Braido",
      "reportDescription": "",
      "location": {
        "x": -46.579607,
        "y": -23.628268
      },
      "pubMillis": 1755264428000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 5,
      "reportByMunicipalityUser": "False",
      "confidence": 3,
      "reliability": 10,
      "type": "ROAD_CLOSED",
      "uuid": "ab10d4e0-57e3-4e22-981e-2e8e17fff1ed",
      "roadType": 2,
      "magvar": 61,
      "subtype": "ROAD_CLOSED_EVENT",
      "street": "Av. Nelson Braido",
      "reportDescription": "",
      "location": {
        "x": -46.581041,
        "y": -23.627868
      },
      "pubMillis": 1755264428000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 5,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 6,
      "type": "ROAD_CLOSED",
      "uuid": "589fc8a7-35b6-4664-af50-36a815b24cd8",
      "roadType": 2,
      "magvar": 113,
      "subtype": "ROAD_CLOSED_EVENT",
      "street": "Av. Nelson Braido",
      "reportDescription": "",
      "location": {
        "x": -46.578719,
        "y": -23.628599
      },
      "pubMillis": 1755264428000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 2,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "JAM",
      "uuid": "4b89b377-96d0-4d58-9afc-7a9c70e6dde7",
      "roadType": 2,
      "magvar": 12,
      "subtype": "JAM_STAND_STILL_TRAFFIC",
      "street": "Av. Guido Aliberti",
      "location": {
        "x": -46.58149,
        "y": -23.630195
      },
      "pubMillis": 1757418124000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 3,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "JAM",
      "uuid": "317089e7-f5f3-4ab7-8996-e727b22e028b",
      "roadType": 2,
      "magvar": 9,
      "subtype": "JAM_STAND_STILL_TRAFFIC",
      "street": "Av. Guido Aliberti",
      "location": {
        "x": -46.582016,
        "y": -23.623479
      },
      "pubMillis": 1757417693000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 4,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "JAM",
      "uuid": "6bef59b6-ceb5-4ab6-ab54-64eb106e567c",
      "roadType": 2,
      "magvar": 323,
      "subtype": "",
      "street": "Av. Pres. Kennedy",
      "location": {
        "x": -46.558156,
        "y": -23.64092
      },
      "pubMillis": 1757416696000
    },
    {
      "country": "BR",
      "city": "São Paulo",
      "reportRating": 0,
      "reportByMunicipalityUser": "False",
      "confidence": 1,
      "reliability": 8,
      "type": "ROAD_CLOSED",
      "uuid": "91163fe5-8eb5-4be5-879f-01d3fa986473",
      "roadType": 2,
      "magvar": 271,
      "subtype": "",
      "street": "Av. Alm. Delamare",
      "reportDescription": "",
      "location": {
        "x": -46.58016,
        "y": -23.611798
      },
      "pubMillis": 1756903498000
    },
    {
      "country": "BR",
      "city": "São Paulo",
      "reportRating": 3,
      "reportByMunicipalityUser": "False",
      "confidence": 1,
      "reliability": 7,
      "type": "JAM",
      "uuid": "c369fc43-a619-4879-9523-b4f9dddd8753",
      "roadType": 2,
      "magvar": 271,
      "subtype": "JAM_STAND_STILL_TRAFFIC",
      "street": "Av. Alm. Delamare",
      "location": {
        "x": -46.580495,
        "y": -23.611793
      },
      "pubMillis": 1757416854000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 1,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "JAM",
      "uuid": "2321f365-598f-40cc-b781-f09069012a90",
      "roadType": 2,
      "magvar": 177,
      "subtype": "JAM_HEAVY_TRAFFIC",
      "street": "R. José Paolone",
      "location": {
        "x": -46.567924,
        "y": -23.615774
      },
      "pubMillis": 1757416882000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 2,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "JAM",
      "uuid": "ccb463fc-0d18-4fb7-832e-eb97002a5280",
      "roadType": 2,
      "magvar": 271,
      "subtype": "JAM_HEAVY_TRAFFIC",
      "street": "Av. Goiás",
      "location": {
        "x": -46.575803,
        "y": -23.615207
      },
      "pubMillis": 1757416948000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 3,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "JAM",
      "uuid": "b08eb10e-39eb-40b0-98f0-5c02c275dd3f",
      "roadType": 2,
      "magvar": 24,
      "subtype": "JAM_STAND_STILL_TRAFFIC",
      "street": "Pç. Luís Ventura",
      "location": {
        "x": -46.579855,
        "y": -23.612668
      },
      "pubMillis": 1757417902000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 3,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "JAM",
      "uuid": "7c7801d1-229a-4cb1-b7e5-669b1a93cc2f",
      "roadType": 2,
      "magvar": 271,
      "subtype": "JAM_STAND_STILL_TRAFFIC",
      "street": "R. Alagoas",
      "location": {
        "x": -46.579956,
        "y": -23.611802
      },
      "pubMillis": 1757418013000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 2,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 6,
      "type": "JAM",
      "uuid": "fb56d1de-ab6e-460e-864b-3d43469ae106",
      "roadType": 2,
      "magvar": 271,
      "subtype": "",
      "street": "Av. Goiás",
      "location": {
        "x": -46.567855,
        "y": -23.616289
      },
      "pubMillis": 1757417894000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 4,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "JAM",
      "uuid": "87eb518a-1fb4-4316-9c02-41e0731f2a75",
      "roadType": 2,
      "magvar": 264,
      "subtype": "JAM_STAND_STILL_TRAFFIC",
      "street": "R. Humaitá",
      "location": {
        "x": -46.567054,
        "y": -23.607135
      },
      "pubMillis": 1757417339000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 1,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "HAZARD",
      "uuid": "768124f6-f445-4dd7-a33d-82b3a6e60385",
      "roadType": 2,
      "magvar": 58,
      "subtype": "HAZARD_ON_ROAD_CONSTRUCTION",
      "street": "Av. dos Estados",
      "location": {
        "x": -46.555547,
        "y": -23.611623
      },
      "pubMillis": 1757418169000
    },
    {
      "country": "BR",
      "city": "São Caetano do Sul",
      "reportRating": 3,
      "reportByMunicipalityUser": "False",
      "confidence": 0,
      "reliability": 5,
      "type": "HAZARD",
      "uuid": "6ac9844e-3fe4-4790-b261-e5a63be3f011",
      "roadType": 2,
      "magvar": 41,
      "subtype": "HAZARD_ON_ROAD_CONSTRUCTION",
      "street": "Av. dos Estados",
      "location": {
        "x": -46.55258,
        "y": -23.608338
      },
      "pubMillis": 1757416816000
    }
  ],
  "endTimeMillis": 1757418060000,
  "irregularities": [
    {
      "country": "BR",
      "nThumbsUp": 0,
      "updateDate": "Tue Sep 9 11:43:26 +0000 2025",
      "trend": 1,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.581363,
          "y": -23.64255
        },
        {
          "x": -46.580993,
          "y": -23.642827
        },
        {
          "x": -46.580754,
          "y": -23.643025
        },
        {
          "x": -46.580452,
          "y": -23.643303
        },
        {
          "x": -46.580189,
          "y": -23.643563
        },
        {
          "x": -46.579847,
          "y": -23.643933
        },
        {
          "x": -46.579669,
          "y": -23.644127
        },
        {
          "x": -46.579002,
          "y": -23.644814
        },
        {
          "x": -46.579002,
          "y": -23.644813
        },
        {
          "x": -46.578593,
          "y": -23.645252
        },
        {
          "x": -46.578024,
          "y": -23.645874
        },
        {
          "x": -46.577428,
          "y": -23.646473
        },
        {
          "x": -46.576953,
          "y": -23.646978
        },
        {
          "x": -46.5767,
          "y": -23.647215
        }
      ],
      "detectionDateMillis": 1757413502658,
      "type": "SMALL",
      "endNode": "Est. das Lágrimas",
      "speed": 6.15,
      "seconds": 411,
      "street": "Av. Guido Aliberti",
      "jamLevel": 4,
      "id": 1624068148,
      "nComments": 0,
      "highway": False,
      "delaySeconds": 342,
      "severity": 5,
      "driversCount": 146,
      "alertsCount": 0,
      "length": 703,
      "updateDateMillis": 1757418206089,
      "nImages": 0,
      "alerts": [],
      "detectionDate": "Tue Sep 9 10:25:02 +0000 2025",
      "regularSpeed": 15.42
    }
  ],
  "startTimeMillis": 1757418000000,
  "startTime": "2025-09-09 11:40:00:000",
  "endTime": "2025-09-09 11:41:00:000",
  "jams": [
    {
      "country": "BR",
      "level": 3,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.569383,
          "y": -23.624514
        },
        {
          "x": -46.569387,
          "y": -23.623994
        },
        {
          "x": -46.569395,
          "y": -23.623006
        },
        {
          "x": -46.569399,
          "y": -23.62253
        },
        {
          "x": -46.569406,
          "y": -23.622032
        },
        {
          "x": -46.569435,
          "y": -23.621064
        }
      ],
      "speedKMH": 9.04,
      "length": 382,
      "turnType": "NONE",
      "uuid": 1637200596,
      "endNode": "R. Maranhão",
      "speed": 2.51111111111111,
      "segments": [
        {
          "fromNode": 158508368,
          "ID": 154726386,
          "toNode": 158508472,
          "isForward": True
        },
        {
          "fromNode": 158508472,
          "ID": 154726381,
          "toNode": 158508151,
          "isForward": True
        },
        {
          "fromNode": 158508151,
          "ID": 335218403,
          "toNode": 268058727,
          "isForward": True
        },
        {
          "fromNode": 268058727,
          "ID": 335218404,
          "toNode": 158508108,
          "isForward": True
        },
        {
          "fromNode": 158508108,
          "ID": 154726368,
          "toNode": 158508104,
          "isForward": True
        }
      ],
      "roadType": 2,
      "delay": 94,
      "street": "R. Amazonas",
      "id": 1637200596,
      "pubMillis": 1757418049395
    },
    {
      "country": "BR",
      "level": 3,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.556527,
          "y": -23.629665
        },
        {
          "x": -46.555772,
          "y": -23.630922
        },
        {
          "x": -46.555535,
          "y": -23.631317
        }
      ],
      "speedKMH": 6.15,
      "length": 209,
      "turnType": "NONE",
      "uuid": 1637781468,
      "endNode": "R. Paraguassú",
      "speed": 1.70833333333333,
      "segments": [
        {
          "fromNode": 158513256,
          "ID": 154733501,
          "toNode": 158513320,
          "isForward": True
        },
        {
          "fromNode": 158513320,
          "ID": 154733986,
          "toNode": 158513402,
          "isForward": True
        }
      ],
      "roadType": 1,
      "delay": 86,
      "street": "Al. Conde de Porto Alegre",
      "id": 1637781468,
      "pubMillis": 1757418206657
    },
    {
      "country": "BR",
      "level": 2,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.565704,
          "y": -23.626012
        },
        {
          "x": -46.565698,
          "y": -23.627024
        },
        {
          "x": -46.565691,
          "y": -23.628104
        },
        {
          "x": -46.565696,
          "y": -23.628974
        }
      ],
      "speedKMH": 9.32,
      "length": 328,
      "turnType": "NONE",
      "uuid": 1637049942,
      "endNode": "R. Ingá",
      "speed": 2.58888888888889,
      "segments": [
        {
          "fromNode": 158509349,
          "ID": 154728236,
          "toNode": 158509348,
          "isForward": True
        },
        {
          "fromNode": 158509348,
          "ID": 154728242,
          "toNode": 158509352,
          "isForward": True
        },
        {
          "fromNode": 158509352,
          "ID": 154728250,
          "toNode": 229635581,
          "isForward": True
        }
      ],
      "roadType": 1,
      "delay": 64,
      "street": "R. Nossa Senhora de Fátima",
      "id": 1637049942,
      "pubMillis": 1757417973250
    },
    {
      "country": "BR",
      "level": 5,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.578719,
          "y": -23.628599
        },
        {
          "x": -46.57853,
          "y": -23.628673
        },
        {
          "x": -46.578285,
          "y": -23.628823
        }
      ],
      "speedKMH": 0,
      "length": 51,
      "turnType": "NONE",
      "uuid": 146908366,
      "endNode": "R. Primeiro de Maio",
      "speed": 0,
      "segments": [
        {
          "fromNode": 158505256,
          "ID": 249568201,
          "toNode": 211859977,
          "isForward": False
        }
      ],
      "blockingAlertUuid": "589fc8a7-35b6-4664-af50-36a815b24cd8",
      "roadType": 2,
      "delay": -1,
      "street": "Av. Nelson Braido",
      "id": 146908366,
      "pubMillis": 1756797334227
    },
    {
      "country": "BR",
      "level": 2,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.553399,
          "y": -23.639019
        },
        {
          "x": -46.554357,
          "y": -23.639511
        },
        {
          "x": -46.555314,
          "y": -23.640001
        },
        {
          "x": -46.556009,
          "y": -23.640355
        },
        {
          "x": -46.556286,
          "y": -23.640463
        }
      ],
      "speedKMH": 9.99,
      "length": 336,
      "turnType": "NONE",
      "uuid": 1637722700,
      "endNode": "Al. Conde de Porto Alegre",
      "speed": 2.775,
      "segments": [
        {
          "fromNode": 158514325,
          "ID": 154734954,
          "toNode": 158513916,
          "isForward": True
        },
        {
          "fromNode": 158513916,
          "ID": 154734316,
          "toNode": 158513472,
          "isForward": True
        },
        {
          "fromNode": 158513472,
          "ID": 154733670,
          "toNode": 158513193,
          "isForward": True
        }
      ],
      "roadType": 1,
      "delay": 64,
      "street": "R. Arlindo Marchetti",
      "id": 1637722700,
      "pubMillis": 1757418207710
    },
    {
      "country": "BR",
      "level": 5,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.569304,
          "y": -23.63246
        },
        {
          "x": -46.570526,
          "y": -23.632011
        }
      ],
      "speedKMH": 0,
      "length": 134,
      "turnType": "NONE",
      "uuid": 1338764824,
      "endNode": "R. Maria Teixeira Mourão Maresti",
      "speed": 0,
      "segments": [
        {
          "fromNode": 244811917,
          "ID": 298582575,
          "toNode": 244811977,
          "isForward": True
        }
      ],
      "blockingAlertUuid": "80e88c83-a403-4dd8-bbaf-e26fb9657a27",
      "roadType": 2,
      "delay": -1,
      "street": "Av. Fernando Simonsen",
      "id": 1338764824,
      "pubMillis": 1757405254586
    },
    {
      "country": "BR",
      "level": 3,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.549752,
          "y": -23.621399
        },
        {
          "x": -46.550695,
          "y": -23.621975
        },
        {
          "x": -46.551175,
          "y": -23.622265
        },
        {
          "x": -46.551637,
          "y": -23.622546
        },
        {
          "x": -46.55258,
          "y": -23.623134
        }
      ],
      "speedKMH": 5.77,
      "length": 347,
      "turnType": "NONE",
      "uuid": 1630148030,
      "endNode": "R. Flórida",
      "speed": 1.60277777777778,
      "segments": [
        {
          "fromNode": 158516053,
          "ID": 154737442,
          "toNode": 158515640,
          "isForward": True
        },
        {
          "fromNode": 158515640,
          "ID": 154737131,
          "toNode": 158515618,
          "isForward": True
        },
        {
          "fromNode": 158515618,
          "ID": 154736813,
          "toNode": 158515168,
          "isForward": True
        },
        {
          "fromNode": 158515168,
          "ID": 154736139,
          "toNode": 158514920,
          "isForward": True
        }
      ],
      "roadType": 1,
      "delay": 149,
      "street": "R. Tapajós",
      "id": 1630148030,
      "pubMillis": 1757415699042
    },
    {
      "country": "BR",
      "level": 3,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.570247,
          "y": -23.607675
        },
        {
          "x": -46.570288,
          "y": -23.606339
        },
        {
          "x": -46.570364,
          "y": -23.605315
        },
        {
          "x": -46.570375,
          "y": -23.605173
        },
        {
          "x": -46.570415,
          "y": -23.604637
        },
        {
          "x": -46.570365,
          "y": -23.604354
        }
      ],
      "speedKMH": 9.75,
      "length": 370,
      "turnType": "NONE",
      "uuid": 1627085286,
      "endNode": "Av. dos Estados",
      "speed": 2.70833333333333,
      "segments": [
        {
          "fromNode": 158508128,
          "ID": 154725953,
          "toNode": 158507983,
          "isForward": True
        },
        {
          "fromNode": 158507983,
          "ID": 154725908,
          "toNode": 158417126,
          "isForward": True
        },
        {
          "fromNode": 158417126,
          "ID": 433755701,
          "toNode": 332091033,
          "isForward": True
        },
        {
          "fromNode": 332091033,
          "ID": 433755702,
          "toNode": 158417100,
          "isForward": True
        },
        {
          "fromNode": 158417100,
          "ID": 154596945,
          "toNode": 158417127,
          "isForward": True
        }
      ],
      "roadType": 1,
      "delay": 74,
      "street": "Av. Conde Francisco Matarazzo",
      "id": 1627085286,
      "pubMillis": 1757414677805
    },
    {
      "country": "BR",
      "level": 5,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.58014,
          "y": -23.62799
        },
        {
          "x": -46.579607,
          "y": -23.628268
        }
      ],
      "speedKMH": 0,
      "length": 62,
      "turnType": "NONE",
      "uuid": 1231427782,
      "endNode": "",
      "speed": 0,
      "segments": [
        {
          "fromNode": 158504804,
          "ID": 154721582,
          "toNode": 158505062,
          "isForward": True
        }
      ],
      "blockingAlertUuid": "07f85a68-3644-453b-b621-3f85cf030cbd",
      "roadType": 2,
      "delay": -1,
      "street": "Av. Nelson Braido",
      "id": 1231427782,
      "pubMillis": 1756139769420
    },
    {
      "country": "BR",
      "level": 5,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.581041,
          "y": -23.627868
        },
        {
          "x": -46.580978,
          "y": -23.627835
        },
        {
          "x": -46.580851,
          "y": -23.627815
        },
        {
          "x": -46.580254,
          "y": -23.627921
        },
        {
          "x": -46.58014,
          "y": -23.62799
        }
      ],
      "speedKMH": 0,
      "length": 97,
      "turnType": "NONE",
      "uuid": 548866580,
      "endNode": "",
      "speed": 0,
      "segments": [
        {
          "fromNode": 158504785,
          "ID": 154721219,
          "toNode": 158504804,
          "isForward": True
        }
      ],
      "blockingAlertUuid": "ab10d4e0-57e3-4e22-981e-2e8e17fff1ed",
      "roadType": 2,
      "delay": -1,
      "street": "Av. Nelson Braido",
      "id": 548866580,
      "pubMillis": 1755931416219
    },
    {
      "country": "BR",
      "level": 2,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.580038,
          "y": -23.632315
        },
        {
          "x": -46.578574,
          "y": -23.633629
        }
      ],
      "speedKMH": 5.11,
      "length": 208,
      "turnType": "NONE",
      "uuid": 1635336026,
      "endNode": "R. Eng. Armando de Arruda Pereira",
      "speed": 1.41944444444444,
      "segments": [
        {
          "fromNode": 158504844,
          "ID": 154721625,
          "toNode": 158505104,
          "isForward": True
        }
      ],
      "roadType": 1,
      "delay": 94,
      "street": "R. Humberto de Campos",
      "id": 1635336026,
      "pubMillis": 1757417425474
    },
    {
      "country": "BR",
      "level": 4,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.574303,
          "y": -23.610004
        },
        {
          "x": -46.5743,
          "y": -23.610499
        },
        {
          "x": -46.574281,
          "y": -23.611837
        }
      ],
      "speedKMH": 4.61,
      "length": 203,
      "turnType": "NONE",
      "uuid": 1637521660,
      "endNode": "R. Alagoas",
      "speed": 1.28055555555556,
      "segments": [
        {
          "fromNode": 158506536,
          "ID": 154724148,
          "toNode": 158506534,
          "isForward": True
        },
        {
          "fromNode": 158506534,
          "ID": 154724140,
          "toNode": 158506531,
          "isForward": True
        }
      ],
      "roadType": 1,
      "delay": 121,
      "street": "R. Pernambuco",
      "id": 1637521660,
      "pubMillis": 1757418130469
    },
    {
      "country": "BR",
      "level": 3,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.557511,
          "y": -23.641724
        },
        {
          "x": -46.558495,
          "y": -23.640495
        },
        {
          "x": -46.558677,
          "y": -23.64027
        },
        {
          "x": -46.558811,
          "y": -23.640074
        },
        {
          "x": -46.558917,
          "y": -23.639851
        },
        {
          "x": -46.559007,
          "y": -23.63958
        },
        {
          "x": -46.559066,
          "y": -23.639185
        },
        {
          "x": -46.559065,
          "y": -23.639122
        },
        {
          "x": -46.559065,
          "y": -23.638992
        },
        {
          "x": -46.559064,
          "y": -23.638992
        },
        {
          "x": -46.559009,
          "y": -23.638579
        }
      ],
      "speedKMH": 8.21,
      "length": 395,
      "turnType": "NONE",
      "uuid": 1633522170,
      "endNode": "",
      "speed": 2.28055555555556,
      "segments": [
        {
          "fromNode": 178282171,
          "ID": 193363817,
          "toNode": 158512238,
          "isForward": True
        },
        {
          "fromNode": 158512238,
          "ID": 180739535,
          "toNode": 172963639,
          "isForward": False
        },
        {
          "fromNode": 172963639,
          "ID": 180739526,
          "toNode": 158512239,
          "isForward": True
        },
        {
          "fromNode": 158512239,
          "ID": 154731864,
          "toNode": 313296568,
          "isForward": True
        }
      ],
      "roadType": 2,
      "delay": 117,
      "street": "Av. Pres. Kennedy",
      "id": 1633522170,
      "pubMillis": 1757416796994
    },
    {
      "country": "BR",
      "level": 5,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.578823,
          "y": -23.628421
        },
        {
          "x": -46.578816,
          "y": -23.628465
        },
        {
          "x": -46.578719,
          "y": -23.628599
        }
      ],
      "speedKMH": 0,
      "length": 23,
      "turnType": "NONE",
      "uuid": 1339851700,
      "endNode": "Av. Nelson Braido",
      "speed": 0,
      "segments": [
        {
          "fromNode": 171163084,
          "ID": 154722187,
          "toNode": 158505256,
          "isForward": True
        }
      ],
      "blockingAlertUuid": "ffb58346-b212-427c-b4e8-994d033796bd",
      "roadType": 1,
      "delay": -1,
      "street": "",
      "id": 1339851700,
      "pubMillis": 1757405128589
    },
    {
      "country": "BR",
      "level": 5,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.579607,
          "y": -23.628268
        },
        {
          "x": -46.579271,
          "y": -23.628424
        },
        {
          "x": -46.578719,
          "y": -23.628599
        }
      ],
      "speedKMH": 0,
      "length": 98,
      "turnType": "NONE",
      "uuid": 1231413194,
      "endNode": "",
      "speed": 0,
      "segments": [
        {
          "fromNode": 158505062,
          "ID": 154721837,
          "toNode": 158505256,
          "isForward": True
        }
      ],
      "blockingAlertUuid": "7b3b485e-d62e-42ed-8eef-b3a2b4d603de",
      "roadType": 2,
      "delay": -1,
      "street": "Av. Nelson Braido",
      "id": 1231413194,
      "pubMillis": 1755264579105
    },
    {
      "country": "BR",
      "level": 3,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.577498,
          "y": -23.611835
        },
        {
          "x": -46.579097,
          "y": -23.611807
        },
        {
          "x": -46.579418,
          "y": -23.611808
        },
        {
          "x": -46.579657,
          "y": -23.611808
        },
        {
          "x": -46.58016,
          "y": -23.611798
        }
      ],
      "speedKMH": 7.29,
      "length": 271,
      "turnType": "NONE",
      "uuid": 1637447848,
      "endNode": "Av. Guido Aliberti",
      "speed": 2.025,
      "segments": [
        {
          "fromNode": 158505447,
          "ID": 154722099,
          "toNode": 158505356,
          "isForward": True
        },
        {
          "fromNode": 158505356,
          "ID": 154721988,
          "toNode": 158505233,
          "isForward": True
        },
        {
          "fromNode": 158505233,
          "ID": 154721803,
          "toNode": 158505064,
          "isForward": True
        },
        {
          "fromNode": 158505064,
          "ID": 415734128,
          "toNode": 158504939,
          "isForward": True
        }
      ],
      "roadType": 2,
      "delay": 83,
      "street": "R. Alagoas",
      "id": 1637447848,
      "pubMillis": 1757418129295
    },
    {
      "country": "BR",
      "level": 3,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.549111,
          "y": -23.62281
        },
        {
          "x": -46.549791,
          "y": -23.623222
        },
        {
          "x": -46.550264,
          "y": -23.623512
        },
        {
          "x": -46.550734,
          "y": -23.6238
        },
        {
          "x": -46.550734,
          "y": -23.623799
        },
        {
          "x": -46.551682,
          "y": -23.624381
        }
      ],
      "speedKMH": 7.59,
      "length": 315,
      "turnType": "NONE",
      "uuid": 1636236596,
      "endNode": "R. Flórida",
      "speed": 2.10833333333333,
      "segments": [
        {
          "fromNode": 304170963,
          "ID": 391593023,
          "toNode": 158516052,
          "isForward": True
        },
        {
          "fromNode": 158516052,
          "ID": 154737694,
          "toNode": 158515842,
          "isForward": True
        },
        {
          "fromNode": 158515842,
          "ID": 154737409,
          "toNode": 158515606,
          "isForward": True
        },
        {
          "fromNode": 158515606,
          "ID": 154736794,
          "toNode": 158515167,
          "isForward": True
        }
      ],
      "roadType": 1,
      "delay": 79,
      "street": "R. Oriente",
      "id": 1636236596,
      "pubMillis": 1757417736281
    },
    {
      "country": "BR",
      "level": 3,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.559793,
          "y": -23.637674
        },
        {
          "x": -46.560679,
          "y": -23.637676
        },
        {
          "x": -46.560976,
          "y": -23.637652
        },
        {
          "x": -46.561446,
          "y": -23.637661
        },
        {
          "x": -46.5633,
          "y": -23.637686
        },
        {
          "x": -46.563792,
          "y": -23.637701
        }
      ],
      "speedKMH": 6.24,
      "length": 407,
      "turnType": "NONE",
      "uuid": 1633092516,
      "endNode": "R. Antonieta",
      "speed": 1.73333333333333,
      "segments": [
        {
          "fromNode": 158511577,
          "ID": 154730894,
          "toNode": 158511311,
          "isForward": False
        },
        {
          "fromNode": 158511311,
          "ID": 154730496,
          "toNode": 158510649,
          "isForward": False
        },
        {
          "fromNode": 158510649,
          "ID": 392403640,
          "toNode": 158510107,
          "isForward": False
        }
      ],
      "roadType": 1,
      "delay": 142,
      "street": "R. Aparecida",
      "id": 1633092516,
      "pubMillis": 1757417814241
    },
    {
      "country": "BR",
      "level": 3,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.554615,
          "y": -23.622597
        },
        {
          "x": -46.554394,
          "y": -23.622455
        },
        {
          "x": -46.55396,
          "y": -23.622176
        },
        {
          "x": -46.553486,
          "y": -23.621883
        },
        {
          "x": -46.552539,
          "y": -23.621304
        }
      ],
      "speedKMH": 6.73,
      "length": 255,
      "turnType": "NONE",
      "uuid": 1634743172,
      "endNode": "R. Alegre",
      "speed": 1.86944444444444,
      "segments": [
        {
          "fromNode": 158513797,
          "ID": 154734801,
          "toNode": 158513924,
          "isForward": False
        },
        {
          "fromNode": 158513924,
          "ID": 154734926,
          "toNode": 158514128,
          "isForward": False
        },
        {
          "fromNode": 158514128,
          "ID": 154735211,
          "toNode": 158514333,
          "isForward": False
        },
        {
          "fromNode": 158514333,
          "ID": 154735495,
          "toNode": 158514713,
          "isForward": False
        }
      ],
      "roadType": 1,
      "delay": 73,
      "street": "R. Capeberibe",
      "id": 1634743172,
      "pubMillis": 1757417894389
    },
    {
      "country": "BR",
      "level": 2,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.576443,
          "y": -23.626099
        },
        {
          "x": -46.578771,
          "y": -23.626092
        }
      ],
      "speedKMH": 6.64,
      "length": 238,
      "turnType": "NONE",
      "uuid": 1636515134,
      "endNode": "Al. Faiança",
      "speed": 1.84444444444444,
      "segments": [
        {
          "fromNode": 209919730,
          "ID": 246483080,
          "toNode": 209917613,
          "isForward": False
        }
      ],
      "roadType": 1,
      "delay": 81,
      "street": "Al. Porcelana",
      "id": 1636515134,
      "pubMillis": 1757417814648
    },
    {
      "country": "BR",
      "level": 2,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.572145,
          "y": -23.602985
        },
        {
          "x": -46.570575,
          "y": -23.60396
        },
        {
          "x": -46.570298,
          "y": -23.604134
        },
        {
          "x": -46.570001,
          "y": -23.604324
        },
        {
          "x": -46.568484,
          "y": -23.605262
        },
        {
          "x": -46.568308,
          "y": -23.605384
        },
        {
          "x": -46.568098,
          "y": -23.605529
        },
        {
          "x": -46.566469,
          "y": -23.606788
        },
        {
          "x": -46.566268,
          "y": -23.606929
        }
      ],
      "speedKMH": 17.59,
      "length": 742,
      "turnType": "NONE",
      "uuid": 1636775032,
      "endNode": "R. Aquidaban",
      "speed": 4.88611111111111,
      "segments": [
        {
          "fromNode": 158415505,
          "ID": 154595227,
          "toNode": 158415944,
          "isForward": True
        },
        {
          "fromNode": 158415944,
          "ID": 252487507,
          "toNode": 158417091,
          "isForward": True
        },
        {
          "fromNode": 158417091,
          "ID": 154596993,
          "toNode": 158417134,
          "isForward": True
        },
        {
          "fromNode": 158417134,
          "ID": 433755674,
          "toNode": 332091018,
          "isForward": True
        },
        {
          "fromNode": 332091018,
          "ID": 433755675,
          "toNode": 158417273,
          "isForward": True
        },
        {
          "fromNode": 158417273,
          "ID": 242631976,
          "toNode": 158418184,
          "isForward": True
        }
      ],
      "roadType": 2,
      "delay": 88,
      "street": "Av. dos Estados",
      "id": 1636775032,
      "pubMillis": 1757417895107
    },
    {
      "country": "BR",
      "level": 4,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.581363,
          "y": -23.64255
        },
        {
          "x": -46.580993,
          "y": -23.642827
        },
        {
          "x": -46.580754,
          "y": -23.643025
        },
        {
          "x": -46.580452,
          "y": -23.643303
        },
        {
          "x": -46.580189,
          "y": -23.643563
        },
        {
          "x": -46.579847,
          "y": -23.643933
        },
        {
          "x": -46.579669,
          "y": -23.644127
        },
        {
          "x": -46.579002,
          "y": -23.644814
        },
        {
          "x": -46.579002,
          "y": -23.644813
        },
        {
          "x": -46.578593,
          "y": -23.645252
        },
        {
          "x": -46.578024,
          "y": -23.645874
        },
        {
          "x": -46.577428,
          "y": -23.646473
        },
        {
          "x": -46.576953,
          "y": -23.646978
        },
        {
          "x": -46.5767,
          "y": -23.647215
        }
      ],
      "speedKMH": 6.15,
      "length": 703,
      "turnType": "NONE",
      "uuid": 1624068148,
      "endNode": "Est. das Lágrimas",
      "speed": 1.70833333333333,
      "segments": [
        {
          "fromNode": 278352053,
          "ID": 351609489,
          "toNode": 158504709,
          "isForward": False
        },
        {
          "fromNode": 158504709,
          "ID": 154721692,
          "toNode": 158505154,
          "isForward": True
        },
        {
          "fromNode": 158505154,
          "ID": 154721776,
          "toNode": 158505212,
          "isForward": True
        },
        {
          "fromNode": 158505212,
          "ID": 237467061,
          "toNode": 204157567,
          "isForward": True
        },
        {
          "fromNode": 204157567,
          "ID": 154722318,
          "toNode": 158505600,
          "isForward": True
        },
        {
          "fromNode": 158505600,
          "ID": 234842096,
          "toNode": 202473131,
          "isForward": True
        },
        {
          "fromNode": 202473131,
          "ID": 234842105,
          "toNode": 158505889,
          "isForward": True
        }
      ],
      "roadType": 2,
      "delay": 342,
      "street": "Av. Guido Aliberti",
      "id": 1624068148,
      "pubMillis": 1757413502658
    },
    {
      "country": "BR",
      "level": 1,
      "city": "São Caetano do Sul",
      "line": [
        {
          "x": -46.570998,
          "y": -23.625735
        },
        {
          "x": -46.570979,
          "y": -23.624817
        },
        {
          "x": -46.571562,
          "y": -23.624759
        }
      ],
      "speedKMH": 4.09,
      "length": 162,
      "turnType": "NONE",
      "uuid": 1635394886,
      "endNode": "R. Rio Grande do Sul",
      "speed": 1.13611111111111,
      "segments": [
        {
          "fromNode": 158507764,
          "ID": 154725352,
          "toNode": 158507761,
          "isForward": True
        }
      ],
      "roadType": 1,
      "delay": 61,
      "street": "R. Helena Mussumecci",
      "id": 1635394886,
      "pubMillis": 1757417426217
    }
  ]
}

    
    return jsonify(data)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
