# swap

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&amp;logoColor=white)](https://github.com/rolehippie/swap)
[![General Workflow](https://github.com/rolehippie/swap/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/swap/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/swap/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/swap/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/swap/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/swap/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/swap)](https://github.com/rolehippie/swap/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.swap-blue)](https://galaxy.ansible.com/rolehippie/swap)

Ansible role to create and configure swap storage.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [swap_path](#swap_path)
  - [swap_size](#swap_size)
  - [swap_swappiness](#swap_swappiness)
  - [swap_vfs_cache_pressure](#swap_vfs_cache_pressure)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`


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

## Discovered Tags

**_swap_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
