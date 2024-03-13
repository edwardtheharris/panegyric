---
abstract: This is API documentation for Panegyric.
authors: Xander Harris
date: 2024-03-12
title: panegyric package
---

## panegyric package
<!--
```{autosummary}
:toctree: .

panegyric.text.Text.get_message
panegyric.text.Text.check_send_date
panegyric.text.Text.get_all_messages
panegyric.text.Text.send_message
panegyric.text.Text.write_message
panegyric.text.main
```
-->

### Submodules

```{inheritance-diagram} panegyric.text.Text
```

#### panegyric.text module

```{eval-rst}
.. automodule:: panegyric.text
   :exclude-members: Text
   :show-inheritance:

   .. autoclass:: Text

      .. rubric:: Attributes

      .. autoattribute:: api_key

      .. autoattribute:: current_date

      .. autoattribute:: message

      .. autoattribute:: messages

      .. autoattribute:: message_file_path

      .. autoattribute:: phone

      .. autoattribute:: url

      .. rubric:: Methods

      .. automethod:: __init__

      .. automethod:: get_message

      .. automethod:: check_send_date

      .. automethod:: get_all_messages

      .. automethod:: send_message

      .. automethod:: write_messages

   .. autofunction:: main
```

## Module contents

```{eval-rst}
.. automodule:: panegyric.text
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:
```
