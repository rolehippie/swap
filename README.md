# swap

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/swap) [![Build Status](https://img.shields.io/drone/build/rolehippie/swap/master?logo=drone)](https://cloud.drone.io/rolehippie/swap) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/swap)](https://github.com/rolehippie/swap/blob/master/LICENSE) 

Ansible role to create and configure swap storage. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

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

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
