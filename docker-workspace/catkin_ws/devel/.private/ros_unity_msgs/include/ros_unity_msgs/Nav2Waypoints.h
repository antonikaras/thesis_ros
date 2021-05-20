// Generated by gencpp from file ros_unity_msgs/Nav2Waypoints.msg
// DO NOT EDIT!


#ifndef ROS_UNITY_MSGS_MESSAGE_NAV2WAYPOINTS_H
#define ROS_UNITY_MSGS_MESSAGE_NAV2WAYPOINTS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <ros_unity_msgs/PosData.h>

namespace ros_unity_msgs
{
template <class ContainerAllocator>
struct Nav2Waypoints_
{
  typedef Nav2Waypoints_<ContainerAllocator> Type;

  Nav2Waypoints_()
    : waypoints()  {
    }
  Nav2Waypoints_(const ContainerAllocator& _alloc)
    : waypoints(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::ros_unity_msgs::PosData_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::ros_unity_msgs::PosData_<ContainerAllocator> >::other >  _waypoints_type;
  _waypoints_type waypoints;





  typedef boost::shared_ptr< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> const> ConstPtr;

}; // struct Nav2Waypoints_

typedef ::ros_unity_msgs::Nav2Waypoints_<std::allocator<void> > Nav2Waypoints;

typedef boost::shared_ptr< ::ros_unity_msgs::Nav2Waypoints > Nav2WaypointsPtr;
typedef boost::shared_ptr< ::ros_unity_msgs::Nav2Waypoints const> Nav2WaypointsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator1> & lhs, const ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator2> & rhs)
{
  return lhs.waypoints == rhs.waypoints;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator1> & lhs, const ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ros_unity_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e7484fc48f37a4ca6f72abe1a6fb5de4";
  }

  static const char* value(const ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe7484fc48f37a4caULL;
  static const uint64_t static_value2 = 0x6f72abe1a6fb5de4ULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_unity_msgs/Nav2Waypoints";
  }

  static const char* value(const ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> >
{
  static const char* value()
  {
    return "PosData[] waypoints\n"
"================================================================================\n"
"MSG: ros_unity_msgs/PosData\n"
"float32 x\n"
"float32 y\n"
"float32 yaw\n"
;
  }

  static const char* value(const ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.waypoints);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Nav2Waypoints_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_unity_msgs::Nav2Waypoints_<ContainerAllocator>& v)
  {
    s << indent << "waypoints[]" << std::endl;
    for (size_t i = 0; i < v.waypoints.size(); ++i)
    {
      s << indent << "  waypoints[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::ros_unity_msgs::PosData_<ContainerAllocator> >::stream(s, indent + "    ", v.waypoints[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_UNITY_MSGS_MESSAGE_NAV2WAYPOINTS_H
