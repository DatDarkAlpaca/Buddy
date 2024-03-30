#pragma once
#include <string>
#include <memory>

#include <QFile>
#include <QSettings>

namespace bud
{
	class BuddySettings
	{
	public:
		static void initialize(const QString& filepath, bool overrideSettings = false);

	public:
		static void setValue(QAnyStringView key, const QVariant& value);

		static QString getString(const QString& entry);

		static QStringList getStrings(const QString& entry, const QString& separator = DefaultSeparator);

	private:
		static inline std::unique_ptr<QSettings> s_Settings;

	private:
		static constexpr const char* DefaultSeparator = ",";
	};
}