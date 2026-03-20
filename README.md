# nstk-data

`nstk-data` is the offline data bundle for the `nstk` package.

It ships:

- Orekit data under `nstk_data/orekit-data`
- Cartopy offline raster and Natural Earth assets under `nstk_data/cartopy`

Typical local development flow:

```bash
pip install -e /path/to/nstk-data
pip install -e /path/to/nstk
```

Once published, installing `nstk` will pull in `nstk-data` as a dependency.
