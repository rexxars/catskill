## Catskill

Webservice that deals with skills.

## Usage

### `/rate`

Based on game outcome, get new skill

**POST /rate** (`Content-Type: application/json`)

Request body:
```json
{
  "teams": [
    [
      {"id": 13, "mu": 23.34, "sigma": 0.96},
      {"id": 14, "mu": 20.52, "sigma": 0.96}
    ],
    [
      {"id": 37, "mu": 29.38, "sigma": 0.95},
      {"id": 17, "mu": 19.45, "sigma": 0.97}
    ]
  ]
}
```

- Winning team first
- `id` (player ID) is not required, but allowed
- `mu` default: `25`
- `sigma` default: `8.333333`

Result:
```json
{
  "teams": [
    [
      {
        "id": 13,
        "mu": 23.480385477499908,
        "sigma": 0.9589357381587995
      },
      {
        "id": 14,
        "mu": 20.660385477499908,
        "sigma": 0.9589357381587995
      }
    ],
    [
      {
        "id": 37,
        "mu": 29.24250222769965,
        "sigma": 0.9491173041400933
      },
      {
        "id": 17,
        "mu": 19.306696579549747,
        "sigma": 0.9687519221160511
      }
    ]
  ]
}
```

### `/quality`

Based on team composition and skill, give a percentage of chance to draw

**POST /quality** (`Content-Type: application/json`)

Request body:
```json
{
  "teams": [
    [
      {"id": 13, "mu": 23.34, "sigma": 0.96},
      {"id": 14, "mu": 20.52, "sigma": 0.96}
    ],
    [
      {"id": 37, "mu": 29.38, "sigma": 0.95},
      {"id": 17, "mu": 19.45, "sigma": 0.97}
    ]
  ]
}
```

Result:
```json
{
  "quality": 82.30453079901952
}
```

## License

MIT-licensed. See LICENSE.

