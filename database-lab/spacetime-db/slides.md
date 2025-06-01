---
theme: default
title: Spacetime DB (Slide by AARMN The Limitless)
highlighter: shiki
drawings:
  persist: false
transition: slide-up
mdc: true
---

<div class="wallpaper-bg"></div>

<div class="video-bg">
  <video autoplay loop muted playsinline>
    <source src="./art.mp4" type="video/mp4">
  </video>
</div>

<div class="content-overlay">
  <h1>Spacetime DB</h1>
  <p>Just a new database for game devs or a new software development paradigm?</p>
  <p>A breeze of fresh air to RDBMS ecosystem, with unique takes</p>
</div>

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}

.video-bg {
  position: absolute;
  top: 0;
  left: 30vw;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.wallpaper-bg {
  position: absolute;
  background-color: #050505;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  object-fit: cover;
}

.video-bg video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.content-overlay {
  position: relative;
  z-index: 2;
  color: white; /* Ensure text is visible against video */
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7); /* Optional: add shadow for better readability */
  padding: 0rem;
}
</style>

---
transition: fade-out
layout: center
---

# Why Spacetime DB?

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>

---
layout: center
---

# 1. Rust

built using a fast programming language for a critical realm

<br>
<br>

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>

---
layout: center
---

# 2. Collaboration in mind

A paradigm changing approach which let end-users connect to DB safely using reducers

<br>
<br>

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>

---
layout: center
---

# 3. WASM

To make running reducers in cloud possible, it uses web-assembly, to ensure rust-based logic can run on any processor, while maintaining beauties of a typed programming language and provide flexibility of an interpreted one

<br>
<br>

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>

---
layout: center
---

# Let's take a look

To make running reducers in cloud possible, it uses web-assembly, to ensure rust-based logic can run on any processor, while maintaining beauties of a typed programming language and provide flexibility of an interpreted one

```rust
use spacetimedb::{table, reducer, ReducerContext, Table};

#[table(name = person, public)]
pub struct Person {
    name: String,
}

#[reducer]
pub fn add(ctx: &ReducerContext, name: String) {
    log::info!("Inserting {}", name);
    ctx.db.person().insert(Person { name });
}

#[reducer]
pub fn say_hello(ctx: &ReducerContext) {
    for person in ctx.db.person().iter() {
        log::info!("Hello, {}!", person.name);
    }
    log::info!("Hello, World!");
}

```

<br>
<br>

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>

---
layout: center
---

# What we infer from this code?

<v-clicks>

- Integrated
- Safe and ACID
- ACID while multithreading
- Less latency
- Logic on DB

</v-clicks>

<br>
<br>

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>

<!--
No middleware, fast,
-->

---
layout: center
---

# 4. Space and Time!

Time-Travel Capability, Stores a full transaction history, allowing state reconstruction at any point in time via replay, akin to time-travel.

<br>
<br>

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>

---
layout: center
---

# 5. Great DX, in CLI and ORM

`spacetime publish app` is all you need to publish your app, and you never deal with sql manually, as you write the API user interacts with, not SQL

<br>
<br>

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>

---
layout: center
---

# SpacetimeDB: Define table

```rust
// Defining tables with indexes
#[table(name = game_object, public)]
pub struct GameObject {
    #[primary_key]
    id: u64,
    #[index]
    owner: Identity,
    position: (f32, f32),
}
```

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>


---
layout: center
---

# SpacetimeDB: Access control

```rust
#[reducer]
pub fn update_position(ctx: &ReducerContext, id: u64, x: f32, y: f32) -> Result<(), String> {
    let caller = ctx.sender;
    let object = ctx.db.game_object().get(&id).ok_or("Not found")?;
    
    // Only allow owner to update their objects
    if object.owner != caller {
        return Err("Unauthorized: You don't own this object".into());
    }
    
    ctx.db.game_object().update(GameObject {
        id,
        owner: object.owner,
        position: (x, y),
    })?;
    
    Ok(())
}
```


<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>

---
layout: center
---

# SpacetimeDB: Advanced Permissions

```rust
#[table]
pub struct Permission {
    #[primary_key]
    identity: Identity,
    role: String, // e.g., "admin", "moderator", "user"
}

#[reducer]
pub fn admin_action(ctx: &ReducerContext, target_id: u64) -> Result<(), String> {
    let caller = ctx.sender;
    
    // Check if caller has admin permissions
    let permission = ctx.db.permission()
        .filter_by_identity(&caller)
        .get()
        .ok_or("User has no permissions")?;
        
    if permission.role != "admin" {
        return Err("Unauthorized: Admin access required".into());
    }
    
    // Perform privileged admin action
    // ...
    
    Ok(())
}
```

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>


---
layout: two-cols
---

# Key Features

<v-clicks>

- **Identity-based access control**
- **Indexes for performance**
- **Ownership tracking**
- **Error handling**
- **Atomic transactions**

</v-clicks>

::right::

# Common Patterns

<v-clicks>

- Store user identity with data
- Check caller in reducers
- Use Result for error handling
- Define clear table relationships
- Keep reducers focused on one task

</v-clicks>

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>


---
layout: center
---

# Thanks for Your Attention!
It's all you need!

<style>
h1, h2, h3, h4, h5, h6, p, li, a, span, div {
  font-family: 'iMWritingMono Nerd Font', monospace !important;
}
</style>


