const tl = gsap.timeline({ defaults: { ease: "power1.out" } });

// tl.to(".text", { y: "0%", duration: 1, stagger: 0.25 });
// tl.to(".slider", { y: "-100%", duration: 1.5, delay: 0.5 });
// tl.to(".intro", { y: "-100%", duration: 1 }, "-=1.2");
tl.fromTo("nav", { opacity: 0 }, { opacity: 1, duration: 1 });
tl.fromTo(".big-text", { opacity: 0 }, { opacity: 1, duration: 1 }, "=-1");
tl.fromTo(".middle-navigation", { color: "#262626", opacity: 0 }, { color:"white",opacity: 1, duration: 1.5 });
// tl.fromTo("a span.middle", { background: "#262626", opacity: 0 }, { background:"linear-gradient(to left,#262626,#ff5245)",opacity: 1, duration: 0.1 },"-1");
// tl.fromTo("a span", { color: "#262626", opacity: 0 }, { color:"white",opacity: 1, duration: 0.1 });