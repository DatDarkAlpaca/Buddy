#include "pch.hpp"
#include "buddy_settings.hpp"
#include "buddy_stylesheet.hpp"

namespace bud
{
	BuddyStylesheet::BuddyStylesheet(QObject* parent)
		: QObject(parent)
	{
		m_Stylesheet = std::make_unique<acss::QtAdvancedStylesheet>();
		initializeStylesheet();
	}

	void BuddyStylesheet::initialize()
	{
		if (!s_Instance)
			s_Instance = new BuddyStylesheet;

		auto currentTheme = s_Instance->stylesheet()->isCurrentThemeDark();
		BuddySettings::setValue("styles/themes/is_theme_dark", currentTheme);
	}

	void BuddyStylesheet::initializeStylesheet()
	{
		QString absoluteStylePath = BuddySettings::getString("paths/style_path");
		QString absoluteStyleOutPath = BuddySettings::getString("paths/style_output_path");

		m_Stylesheet->setStylesDirPath(absoluteStylePath);
		m_Stylesheet->setOutputDirPath(absoluteStyleOutPath);

		auto currentStyle = BuddySettings::getString("styles/themes/selected_style");
		auto currentTheme = BuddySettings::getString("styles/themes/selected_theme");

		m_Stylesheet->setCurrentStyle(currentStyle);
		m_Stylesheet->setCurrentTheme(currentTheme);
		m_Stylesheet->updateStylesheet();

		qApp->setStyleSheet(m_Stylesheet->styleSheet());
	}
}