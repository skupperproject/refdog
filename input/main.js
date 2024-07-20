// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

Element.prototype.$ = function () {
    return this.querySelector.apply(this, arguments);
};

Element.prototype.$$ = function () {
    return this.querySelectorAll.apply(this, arguments);
};

// window.$ = $;
// window.$$ = $$;

// document.addEventListener("DOMContentLoaded", function() {
//     function showSectionFromFragment() {
//         const sections = $$("section");
//         const fragment = window.location.hash.substring(1);

// 	for (const section of sections) {
// 	    if (section.$("h3")) {
//                 if (section.$("h3").id === fragment) {
//                     section.classList.remove("hidden");
//                 } else {
//                     section.classList.add("hidden");
//                 }
// 	    }
//         }
//     }

//     // Show the section on initial load
//     showSectionFromFragment();

//     // Show the section whenever the hash changes
//     window.addEventListener("hashchange", showSectionFromFragment);
// });

window.addEventListener("load", () => {
    const oldToc = $("#-toc");

    if (!oldToc) {
        return;
    }

    const headings = $$("h2");

    if (headings.length == 0) {
	oldToc.remove();
        return;
    }

    const newToc = document.createElement("section");
    const newTocHeading = document.createElement("h4");
    const newTocHeadingText = document.createTextNode("Contents");

    newTocHeading.appendChild(newTocHeadingText);
    newToc.appendChild(newTocHeading);
    newToc.setAttribute("id", "-toc");

    const newTocLinks = document.createElement("nav");

    const topLink = document.createElement("a");
    const topText = document.createTextNode("Top");

    topLink.setAttribute("href", "#");
    topLink.appendChild(topText);

    newTocLinks.appendChild(topLink);

    for (const heading of headings) {
        const link = document.createElement("a");
        const text = document.createTextNode(heading.textContent);

        link.setAttribute("href", `#${heading.id}`);
        link.appendChild(text);

        newTocLinks.appendChild(link);
    }

    newToc.appendChild(newTocLinks);
    oldToc.replaceWith(newToc);
});

window.addEventListener("load", () => {
    const tocLinks = $("#-toc nav");

    if (!tocLinks) {
        return;
    }

    const updateHeadingSelection = () => {
        const currHash = window.location.hash;

        if (!currHash) {
	    const link = tocLinks.$("a");

	    link.classList.add("selected");

            for (const link of tocLinks.$$("a:not(:first-child)")) {
                link.classList.remove("selected");
            }

            return;
        }

        for (const link of tocLinks.$$("a")) {
            const linkHash = new URL(link.href).hash;

            if (linkHash === currHash) {
                link.classList.add("selected");
            } else {
                link.classList.remove("selected");
            }
        }
    }

    updateHeadingSelection();

    window.addEventListener("hashchange", updateHeadingSelection);
});

// window.addEventListener("load", () => {
//     const updateScrollState = () => {
//         if (window.scrollY > 20) {
//             $("body").classList.add("scrolled");
//         } else {
//             $("body").classList.remove("scrolled");
//         }
//     };

//     updateScrollState();
//     window.addEventListener("scroll", updateScrollState);
// });
