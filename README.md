# nebula-data

`nebula-data` is the offline data bundle for the `nebula` package.

It ships:

- Orekit data under `nebula_data/orekit-data`
- Cartopy offline raster and Natural Earth assets under `nebula_data/cartopy`

Typical local development flow:

```bash
pip install -e /path/to/nebula-data
pip install -e /path/to/Nebula
```

Once published, installing `nebula` will pull in `nebula-data` as a dependency.
