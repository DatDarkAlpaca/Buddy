#include "pch.hpp"
#include "constants.hpp"
#include "buddy_settings.hpp"

namespace bud
{
	static void createProjectSettings(QSettings& settings)
	{
		settings.setValue("project/extension", "prj");
		settings.setValue("project/directory", "");
		settings.setValue("project/supported/media_formats", "gif,png,jpg,webp");
	}

	static void createStyleSettings(QSettings& settings)
	{
		// Themes:
		settings.setValue("styles/themes/selected_style", "buddy_material");
		settings.setValue("styles/themes/selected_theme", "dark_purple");
		settings.setValue("styles/themes/is_theme_dark", true);

		// Subtitles:
		settings.setValue("styles/subtitles/override_styles", false);
		settings.setValue("styles/subtitles/primary/font_family", "segoe ui");
		settings.setValue("styles/subtitles/primary/font_size", 12);
		settings.setValue("styles/subtitles/primary/font_color", "#FFFFFFFF");
		settings.setValue("styles/subtitles/primary/font_background_color", "#000000C0");

		// Buddy:
		settings.setValue("styles/min_image_width_pixels", "10");
		settings.setValue("styles/min_image_height_pixels", "10");

		settings.setValue("styles/max_image_width_percentage", "70");
		settings.setValue("styles/max_image_height_percentage", "50");
	}

	static void createPathSettings(QSettings& settings)
	{
		settings.setValue("paths/resources_folder", "res");
		settings.setValue("paths/style_path", "res/styles");
		settings.setValue("paths/style_output_path", "res/output");
		settings.setValue("paths/plugin_path", "plugins");
	}

	static void createIconSettings(QSettings& settings)
	{
		settings.setValue("icons/play_icon", ":/Icons/icons/miftakhul/play.png");
		settings.setValue("icons/pause_icon", ":/Icons/icons/miftakhul/pause.png");
		settings.setValue("icons/max_volume", ":/Icons/icons/miftakhul/volume_full.png");
		settings.setValue("icons/normal_volume", ":/Icons/icons/miftakhul/volume_two.png");
		settings.setValue("icons/muted_volume", ":/Icons/icons/miftakhul/volume_none.png");
	}

	static void createDefaultSettings(QSettings& settings)
	{
		settings.setValue("version", bud::ProjectVersion);

		createProjectSettings(settings);

		createStyleSettings(settings);

		createPathSettings(settings);

		createIconSettings(settings);

		settings.sync();
	}
}

namespace bud
{
	void BuddySettings::initialize(const QString& filepath, bool overrideSettings)
	{
		s_Settings = std::make_unique<QSettings>(filepath, QSettings::IniFormat);

		if (overrideSettings || !QFile::exists(s_Settings->fileName()))
			createDefaultSettings(*s_Settings);
	}

	void BuddySettings::setValue(QAnyStringView key, const QVariant& value)
	{
		s_Settings->setValue(key, value);
	}

	QString BuddySettings::getString(const QString& entry)
	{
		return s_Settings->value(entry).toString();
	}

	QStringList BuddySettings::getStrings(const QString& entry, const QString& separator)
	{
		return s_Settings->value(entry).toString().split(separator);
	}
}