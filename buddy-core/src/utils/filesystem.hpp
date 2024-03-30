#pragma once
#include <QApplication>
#include <QString>
#include <QDir>

namespace bud::paths
{
	inline QString getAbsoluteAppPath(const QString& filepath)
	{
		return qApp->applicationDirPath() + QDir::separator() + filepath;
	}
}