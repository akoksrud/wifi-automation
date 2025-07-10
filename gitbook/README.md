---
icon: network-wired
---

# Topology

<img src=".gitbook/assets/file.excalidraw (1).svg" alt="Placeholder topology map" class="gitbook-drawing">

```mermaid
graph LR
    A[Client] --> B(Load Balancer)
    B --> C{Server};
    B --> D{Server};
    C --> E[Database];
    D --> E;
```







<div data-full-width="true"><figure><img src=".gitbook/assets/topology.drawio.svg" alt=""><figcaption></figcaption></figure></div>
