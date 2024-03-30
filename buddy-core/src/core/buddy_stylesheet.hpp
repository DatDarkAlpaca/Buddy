#pragma once
#include <memory>
#include <QObject>
#include <QtAdvancedStylesheet.h>

namespace bud
{
	class BuddyStylesheet : public QObject
	{
		Q_OBJECT;

	private:
		explicit BuddyStylesheet(QObject* parent = nullptr);

	public:
		static void initialize();

	private:
		void initializeStylesheet();

	public:
		static inline BuddyStylesheet* instance() { return s_Instance; }

		std::unique_ptr<acss::QtAdvancedStylesheet>& stylesheet() { return m_Stylesheet; }

	private:
		std::unique_ptr<acss::QtAdvancedStylesheet> m_Stylesheet = nullptr;
		static inline BuddyStylesheet* s_Instance = nullptr;
	};
}