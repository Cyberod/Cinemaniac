# Essential Stuff

## Html import links

Google font

``` html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&display=swap" rel="stylesheet">
```

---

## Colors

### Background color

``` css
--background: hsla(220, 17%, 7%, 1);
--banner-background: hsla(250, 6%, 20%, 1);
--white-alpha-20: hsla(0, 0%, 100%, 0.2);
--on-background: hsla(220, 100%, 95%, 1);
--on-surface: hsla(250, 100%, 95%, 1);
--on-surface-variant: hsla(250, 1%, 44%, 1);
--primary: hsla(349, 100%, 43%, 1);
--primary-variant: hsla(349, 69%, 51%, 1);
--rating-color: hsla(44, 100%, 49%, 1);
--surface: hsla(250, 13%, 11%, 1);
--text-color: hsla(250, 2%, 59%, 1);
--white: hsla(0, 0%, 100%, 1);
```

### Gradient color

``` css
--banner-overlay: 90deg, hsl(220, 17%, 7%) 0%, hsla(220, 17%, 7%, 0.5) 100%;
--bottom-overlay: 180deg, hsla(250, 13%, 11%, 0), hsla(250, 13%, 11%, 1);
```

## Typography

``` css
--ff-dm-sans: 'DM Sans', sans-serif;

--fs-heading: 4rem;
--fs-title-lg: 2.6rem;
--fs-title: 2rem;
--fs-body: 1.8rem;
--fs-button: 1.5rem;
--fs-label: 1.4rem;

--weight-bold: 700;
```

## Shadow

``` css
--shadow-1: 0 1px 4px hsla(0, 0%, 0%, 0.75);
--shadow-2: 0 2px 4px hsla(350, 100%, 43%, 0.3);
```

## Border Radius

``` css
--radius-4: 4px;
--radius-8: 8px;
--radius-16: 16px;
--radius-24: 24px;
--radius-36: 36px;
```

## Transition

``` css
--transition-short: 250ms ease;
--transition-long: 500ms ease;
```


NAVBAR

            <div class="navbar">
                <a href="#home" class="nav-link nav-active">
                    <i class="bx bx-home-circle"></i>
                    <span class="nav-link-title">Home</span>
                </a>
                <a href="#home" class="nav-link">
                    <i class="bx bx-compass"></i>
                    <span class="nav-link-title">Explore</span>
                </a>
                <a href="#home" class="nav-link">
                    <i class="bx bxs-hot"></i>
                    <span class="nav-link-title">Trending</span>
                </a>
                <a href="#home" class="nav-link">
                    <i class="bx bx-heart-circle"></i>
                    <span class="nav-link-title">Favourites</span>
                </a>

    
    .nav {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px 0;
}
.navbar {
  position: fixed;
  top: 50%;
  transform: translateY(-50%);
  left: 18px;
  display: flex;
  flex-direction: column;
  row-gap: 2.1rem;  
}
.nav-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #b7b7b7;
}
.nav-link:hover,
.nav-active {
  color: var(--main-color);
  transition: o.3s all linear;
  transform: scale(1.1);
}
.nav-link .bx {
  font-size: 1.6rem;
}
.nav-link-title {
  font-size: 0.7rem;
  font: var(--weight-bold);
}


USER IMAGE
.user {
  display: flex;
}
.user-img {
  width: 10%;
  height: 10%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center;
  margin-inline-start: auto;
}


USER
            <a href="#" class="user">
                <img src="./assets/images/profile.jpg" alt="" class="user-img">
            </a>