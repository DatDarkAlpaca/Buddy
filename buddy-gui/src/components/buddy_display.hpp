#pragma once
#include <vector>
#include <QScreen>
#include <QLabel>
#include <QGuiApplication>
#include <QTimer>
#include <QMovie>
#include <QPixmap>

#include <QDir>
#include <core/buddy_settings.hpp>

namespace bud
{
	class BuddyDisplay : public QLabel
	{
		Q_OBJECT;

	public:
		explicit BuddyDisplay(QWidget* parent = nullptr)
			: QLabel(parent)
		{
		}

	public:
		void setBuddy(const QPixmap& buddyPixmap)
		{
			QSize finalSize = clampBuddySize(buddyPixmap.size());

			setPixmap(buddyPixmap);
			emit buddySet(finalSize);
		}

		void setBuddy(QMovie* buddyMovie)
		{
			QSize finalSize = clampBuddySize(buddyMovie->scaledSize());

			setMovie(buddyMovie);
			emit buddySet(finalSize);

			m_Movie = buddyMovie;
			buddyMovie->start();
		}

	private:
		QSize clampBuddySize(const QSize& imageSize)
		{
			QSize finalSize = imageSize;
			const float aspectRatio = (float)imageSize.width() / (float)imageSize.height();

			QScreen* screen = QGuiApplication::primaryScreen();
			QRect screenGeometry = screen->geometry();

			int minWidth = BuddySettings::getString("styles/min_image_width_pixels").toInt();
			int minHeight = BuddySettings::getString("styles/min_image_height_pixels").toInt();
			int maxWidthPercentage = BuddySettings::getString("styles/max_image_width_percentage").toFloat();
			int maxHeightPercentage = BuddySettings::getString("styles/max_image_height_percentage").toFloat();

			finalSize.setWidth(std::clamp(imageSize.width(), minWidth, int(maxWidthPercentage * 0.01f * screenGeometry.width())));
			finalSize.setHeight(std::clamp(imageSize.height(), minHeight, int(maxHeightPercentage * 0.01f * screenGeometry.height())));

			adjustAspectRatio(finalSize, aspectRatio);
			return finalSize;
		}

		void adjustAspectRatio(QSize& size, float aspectRatio)
		{
			if (size.width() <= size.height())
				size.setHeight(size.width() / aspectRatio);
			else
				size.setWidth(aspectRatio * size.height());
		}

	signals:
		void buddySet(const QSize&);

	private:
		QMovie* m_Movie = nullptr;
		QTimer* m_Timer = nullptr;
	};
}