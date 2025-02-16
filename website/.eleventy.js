export default function (eleventyConfig) {
  eleventyConfig.ignores.add("_logs/**");

  eleventyConfig.addLayoutAlias("post", "default.njk");
  eleventyConfig.addLayoutAlias("page", "default.njk");

  eleventyConfig.addPassthroughCopy("assets");

  eleventyConfig.addPassthroughCopy("**/*.txt");
  eleventyConfig.addPassthroughCopy("**/*.jpg");
  eleventyConfig.addPassthroughCopy("**/*.png");

  eleventyConfig.setServerPassthroughCopyBehavior("passthrough");
  
  function generateImageHtml(params) {
    const imageSrc = params.src 
      ? params.src 
      : `/assets/${params.directory || ''}/${params.name || ''}`;
    
    const captionHtml = params.caption
      ? `<div class="caption">${params.caption}</div>`
      : '';

    return `
      <div class="image-container">
        <img src="${imageSrc}" 
             alt="${params.alt || ''}" 
             ${params.width ? `width="${params.width}"` : ''} 
             ${params.height ? `height="${params.height}"` : ''}>
        ${captionHtml}
      </div>
    `.trim();
  }

  eleventyConfig.addShortcode("image", function (params) {
    return generateImageHtml(params);
  });

  eleventyConfig.addShortcode("unsplashImage", function (params) {
    const unsplashCaption = `
      Photo by <a href="https://unsplash.com/@${params.username}" target="_blank">${params.photographer}</a> 
      from <a href="${params.image_link}" target="_blank">Unsplash</a>
    `;

    return generateImageHtml({
      ...params,
      caption: unsplashCaption,
    });
  });

  return {
    dir: {
      input: ".", // Source folder
      layouts: "_layouts",
      data: "_data",
      output: "_site", // Output folder
    },
    serverOptions: {
      port: 4000,
    },
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
  };
}