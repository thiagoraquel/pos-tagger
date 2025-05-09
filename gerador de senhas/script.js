module.exports = async (tp) => {
  const song = await tp.system.prompt("Song title?");
  const artist = await tp.system.prompt("Artist name?");
  
  const filename = `${artist} - ${song}`;

  await tp.file.create_new(
    await tp.templates.find_tfile("Template"), // template name
    filename
  );
};
