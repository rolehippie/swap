# swap

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/swap/status.svg)](https://cloud.drone.io/rolehippie/swap)

Ansible role to configure swap

## Table of content

* [Default Variables](#default-variables)
  * [swap_path](#swap_path)
  * [swap_size](#swap_size)
  * [swap_swappiness](#swap_swappiness)
  * [swap_vfs_cache_pressure](#swap_vfs_cache_pressure)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### swap_path

Path to the swapfile to create

#### Default value

```YAML
swap_path: /swapfile
```

### swap_size

Size of the swapfile to create

#### Default value

```YAML
swap_size: '{{ ansible_memtotal_mb }}'
```

### swap_swappiness

Set vm.swappiness value

#### Default value

```YAML
swap_swappiness: '10'
```

### swap_vfs_cache_pressure

Set vm.vfs_cache_pressure value

#### Default value

```YAML
swap_vfs_cache_pressure: '50'
```

## Dependencies

None.

## License

Apache-2.0

## Author

Thomas Boerger
