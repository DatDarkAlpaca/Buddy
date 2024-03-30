#include <QApplication>
#include <QSettings>
#include <gui.hpp>

#include <constants.hpp>
#include <utils/filesystem.hpp>
#include <core/buddy_settings.hpp>
#include <core/buddy_stylesheet.hpp>

static void preInitialize()
{
	QSettings::setDefaultFormat(QSettings::IniFormat);
	QApplication::setOrganizationName("DatDarkAlpaca");
	QApplication::setApplicationName("Buddy");
	QCoreApplication::setAttribute(Qt::AA_CompressHighFrequencyEvents);
}

int main(int argc, char** argv)
{
	using namespace bud;
	QApplication* app = new QApplication(argc, argv);

	preInitialize();

	BuddySettings::initialize(paths::getAbsoluteAppPath(SettingsFilename), true);
	BuddyStylesheet::initialize();

	MiniBuddy* buddy = new MiniBuddy;
	{
		QObject::connect(buddy, &MiniBuddy::openBuddyPressed, [&]() {
			QString filepath = openBuddyDialog();

			if (filepath.isEmpty())
				return;

			if (filepath.endsWith(".gif"))
			{
				QMovie* movie = new QMovie(filepath);
				buddy->buddyDisplay()->setBuddy(movie);
			}
			else
			{
				QPixmap pixmap(filepath);
				buddy->buddyDisplay()->setBuddy(pixmap);
			}
		});

		QObject::connect(buddy, &MiniBuddy::closePressed, [&]() {
			exit(0);
			});
	}

	buddy->show();

	app->exec();
	return 0;
}