const tl = gsap.timeline({ defaults: { ease: "power1.out" } });
tl.fromTo(".SignUplink", { opacity: 0 }, { opacity: 1, duration: 1 });
tl.fromTo(".registration-form", { opacity: 0 }, { opacity: 1, duration: 1 }, "-=1");