---
icon: network-wired
---

# Topology

````mermaid
```mermaid
graph LR
    A[Client] --> B(Load Balancer)
    B --> C{Server};
    B --> D{Server};
    C --> E[Database];
    D --> E;
```
````

